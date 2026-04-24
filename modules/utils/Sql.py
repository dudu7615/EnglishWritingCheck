from typing import Optional, Any, Annotated
from datetime import datetime
import sqlite3
import atexit
from pathlib import Path
from sqlmodel import SQLModel, Field, create_engine, Session, select, delete  # type: ignore
from sqlalchemy import text, event, MetaData, Engine, JSON, Column
from sqlalchemy.types import TypeDecorator
from pydantic import BaseModel
from . import DataTypes, Paths

_sqlMetadata = MetaData()
_engine: Optional[Engine] = None


class _PydanticColumn[T: BaseModel](TypeDecorator[T]):
    impl = JSON
    cache_ok = True
    mutable = True  # 自动检测Pydantic实例内部属性修改，无需手动标记脏数据

    def __init__(self, model: type[T], **kwargs: Any):
        super().__init__(**kwargs)
        self.model = model

    def process_bind_param(
        self, value: T | None, dialect: Any
    ) -> dict[str, Any] | None:
        return value.model_dump() if value is not None else None

    def process_result_value(
        self, value: dict[str, Any] | None, dialect: Any
    ) -> T | None:
        return self.model.model_validate(value) if value is not None else None


type _PydanticCol[T: BaseModel] = Annotated[T, _PydanticColumn]


class _Model(SQLModel):
    metadata = _sqlMetadata


class Exam(_Model, table=True):
    """考试记录"""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=200)
    remoteId: str = Field(max_length=200)
    topic: Optional[str] = Field(default=None)  # 考试题目
    answer: Optional[str] = Field(default=None)  # 标准答案
    answerCount: int = Field(default=0)
    createAt: Optional[datetime] = Field(default_factory=datetime.now)

    @staticmethod
    def create(
        name: str,
        remoteId: str,
        topic: Optional[str] = None,
        answer: Optional[str] = None,
        session: Optional[Session] = None,
    ) -> "Exam":
        ownSession = session or getSession()
        try:
            chapter = Exam(name=name, remoteId=remoteId, topic=topic, answer=answer)
            ownSession.add(chapter)
            ownSession.commit()
            ownSession.refresh(chapter)
            return chapter
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def getAll(session: Optional[Session] = None) -> list["Exam"]:
        ownSession = session or getSession()
        try:
            statement = select(Exam).order_by(text("id ASC"))
            results = ownSession.exec(statement).all()
            return list(results)
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def get(nameOrId: str | int, session: Optional[Session] = None) -> Optional["Exam"]:
        if isinstance(nameOrId, int):
            return Exam._getById(nameOrId, session)
        else:
            return Exam._getByTitle(nameOrId, session)

    @staticmethod
    def _getById(chapterId: int, session: Optional[Session] = None) -> Optional["Exam"]:
        ownSession = session or getSession()
        try:
            statement = select(Exam).where(Exam.id == chapterId)
            return ownSession.exec(statement).first()
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def _getByTitle(title: str, session: Optional[Session] = None) -> Optional["Exam"]:
        ownSession = session or getSession()
        try:
            statement = select(Exam).where(Exam.name == title)
            return ownSession.exec(statement).first()
        finally:
            if not session:
                ownSession.close()

    def delete(self, session: Optional[Session] = None):
        ownSession = session or getSession()
        try:
            ownSession.delete(self)
            ownSession.commit()
        finally:
            if not session:
                ownSession.close()


class Papers(_Model, table=True):
    """试卷"""

    id: Optional[int] = Field(default=None, primary_key=True)
    belong: int = Field(index=True, foreign_key="exam.id")  # 对应考试
    img: str = Field()  # 图片路径
    comment: _PydanticCol[DataTypes.ApiReply] = Field(
        default=None, sa_column=Column(_PydanticColumn(DataTypes.ApiReply))
    )  # 批改意见
    createdAt: datetime = Field(default_factory=datetime.now)

    @staticmethod
    def add(belong: int, img: str, session: Optional[Session] = None) -> "Papers":
        ownSession = session or getSession()
        try:
            papers = Papers(belong=belong, img=img)
            ownSession.add(papers)

            if exam := ownSession.get(Exam, belong):
                exam.answerCount += 1
                ownSession.add(exam)

            ownSession.commit()
            ownSession.refresh(papers)
            return papers
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def get(id: int, session: Optional[Session] = None) -> Optional["Papers"]:
        ownSession = session or getSession()
        try:
            return ownSession.get(Papers, id)
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def getByExamId(
        examId: Optional[int], session: Optional[Session] = None
    ) -> list["Papers"]:
        ownSession = session or getSession()
        try:
            statement = select(Papers).where(Papers.belong == examId)
            return list(ownSession.exec(statement).all())
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def getAll(session: Optional[Session] = None) -> list["Papers"]:
        ownSession = session or getSession()
        try:
            statement = select(Papers).order_by(text("id ASC"))
            return list(ownSession.exec(statement).all())
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def mark(
        papersId: int,
        comment: Optional[DataTypes.ApiReply] = None,
        session: Optional[Session] = None,
    ):
        """批改"""
        ownSession = session or getSession()
        try:
            papers = ownSession.get(Papers, papersId)
            if not papers:
                raise ValueError("Papers not found")
            if comment:
                papers.comment = comment
            ownSession.add(papers)
            ownSession.commit()
        finally:
            if not session:
                ownSession.close()

    def delete(self, session: Optional[Session] = None):
        ownSession = session or getSession()
        try:
            # 先获取 belong 值，用于后续更新 Exam
            belong = self.belong

            ownSession.delete(self)
            ownSession.commit()

            if exam := ownSession.get(Exam, belong):
                exam.answerCount = max(0, exam.answerCount - 1)
                ownSession.add(exam)
                ownSession.commit()
        finally:
            if not session:
                ownSession.close()


def initSql(file: Path):
    global _engine
    _sqlite_url = f"sqlite:///{file.as_posix()}"
    _engine = create_engine(
        _sqlite_url,
        connect_args={"check_same_thread": False},
        isolation_level="SERIALIZABLE",
    )

    event.listen(_engine, "connect", _sqlitePragma)
    _sqlMetadata.create_all(_engine)


def getSession():
    return Session(_engine)


def _sqlitePragma(dbapi_connection: sqlite3.Connection, connection_record: Any):  # type: ignore
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.execute("PRAGMA busy_timeout = 5000")
    cursor.close()


def _close_database():
    """关闭数据库连接"""
    if _engine:
        _engine.dispose()


atexit.register(_close_database)

initSql(Paths.data / "data.db")
