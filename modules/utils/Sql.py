from typing import Optional, Any
from datetime import datetime
import sqlite3
import atexit
from pathlib import Path
from sqlmodel import SQLModel, Field, create_engine, Session, select, delete  # type: ignore
from sqlalchemy import text, event, MetaData, Engine, JSON
from . import DataTypes, Paths

_sqlMetadata = MetaData()
_engine: Optional[Engine] = None


class _Model(SQLModel):
    metadata = _sqlMetadata


class Exam(_Model, table=True):
    """考试记录"""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=200)
    remoteId: str = Field(default=None, max_length=200)
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
            result = ownSession.exec(statement).first()
            return result
        finally:
            if not session:
                ownSession.close()

    @staticmethod
    def _getByTitle(title: str, session: Optional[Session] = None) -> Optional["Exam"]:
        ownSession = session or getSession()
        try:
            statement = select(Exam).where(Exam.name == title)
            result = ownSession.exec(statement).first()
            return result
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
    comment: Optional[dict[str, Any]] = Field(default=None, sa_type=JSON)  # 评分
    createdAt: Optional[datetime] = Field(default_factory=datetime.now)

    @staticmethod
    def add(belong: int, img: str, session: Optional[Session] = None) -> "Papers":
        ownSession = session or getSession()
        try:
            papers = Papers(belong=belong, img=img)
            ownSession.add(papers)

            ownSession.commit()
            ownSession.refresh(papers)

            # 更新对应 Exam 的 answerCount
            exam = ownSession.get(Exam, belong)
            if exam:
                exam.answerCount += 1
                ownSession.add(exam)
                ownSession.commit()

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
                papers.comment = dict(comment)
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

            # 更新对应 Exam 的 answerCount
            exam = ownSession.get(Exam, belong)
            if exam:
                exam.answerCount = max(0, exam.answerCount - 1)
                ownSession.add(exam)
                ownSession.commit()
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
