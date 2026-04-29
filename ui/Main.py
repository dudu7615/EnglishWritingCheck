from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog, QMessageBox
from modules import (
    logger,
    uiLogger,
    Sql,
    Paths,
    DataTypes,
    Enums,
    SubThreads,
    HandleApiResult,
)
from pathlib import Path
import shutil
from .Windows import Main_ui
from ui import ShowOptions
import socket


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Main_ui.Ui_MainWindow()
        self.ui.setupUi(self)  # type: ignore
        self.showOptionsUi = ShowOptions.ShowOptionsUi()
        uiLogger.log.connect(self.ui.showLog.append)
        self.showOptionsUi.optionChange.connect(self.showOptionsChanged)

        self.fileServer: SubThreads.FileServerThread | None = None
        self.cloudflare: SubThreads.CloudflareThread | None = None
        self.apiThread: SubThreads.CallApiThread | None = None

        self.cfUrl = ""
        self.showOption = (
            Enums.ShowDetaleOption.word_usage_errors
            | Enums.ShowDetaleOption.advanced_expression_pattern
            | Enums.ShowDetaleOption.advanced_vocabulary
            | Enums.ShowDetaleOption.personalized_sample
            | Enums.ShowDetaleOption.sentence_usage_errors
            | Enums.ShowDetaleOption.tense_usage_errors
        )
        self._initSubThreads()

        self.initUi()

    def initUi(self):
        # 可移动控件显示
        self.ui.showOrHideLog.triggered.connect(
            lambda: self.ui.logBox.setVisible(not self.ui.logBox.isVisible())
        )

        # Exam Page
        self.ui.creatNewExam.clicked.connect(self.createExam)
        self.ui.deleteExam.clicked.connect(self.deleteExam)

        # Paper Page
        self.ui.showDetals.setHtml(HandleApiResult.result2Html())
        self.ui.importPapers.clicked.connect(self.importPapers)
        self.ui.deleteChoosed.clicked.connect(self.deletePapers)
        self.ui.paperList.clicked.connect(self.showPaerAndDetales)
        self.ui.checkChosed.clicked.connect(self.checkChosed)

        self._initExamList()
        self._initPaperList()

    # Exam Page
    def createExam(self):
        Sql.Exam.create(
            name=self.ui.examName.text(), remoteId=self.ui.examRemoteId.text()
        )

        logger.info(f"成功创建考试: {self.ui.examName.text()}")

        self._initExamList()
        self._initPaperList()

    def deleteExam(self):
        currentExam = self.ui.examList.currentItem()
        if currentExam:
            if exam := Sql.Exam.get(currentExam.text()):
                exam.delete()

        logger.info(f"成功删除考试: {currentExam.text()}")

        self._initExamList()
        self._initPaperList()

    # Paper Page
    def importPapers(self):
        currentExam = self.ui.paperList.currentItem()
        if not currentExam:
            QMessageBox.warning(self, "警告", "请先选择一个考试")
            return

        if currentExam.parent():
            examId = int(currentExam.parent().text(0))
        else:
            examId = int(currentExam.text(0))

        files, _ = QFileDialog.getOpenFileNames(
            self, "选取试卷图片", "", "图片 (*.png *.jpg *.jpeg)"
        )

        (Paths.data / "imgs" / str(examId)).mkdir(parents=True, exist_ok=True)

        for file in files:
            shutil.copy2(
                file,
                Paths.data / "imgs" / str(examId) / Path(file).name,
            )

        with Sql.getSession() as session:
            for file in files:
                Sql.Papers.add(
                    belong=examId,
                    img=(Path(str(examId)) / Path(file).name).as_posix(),
                    session=session,
                )

        logger.info(f"成功导入试卷: {len(files)} 张")

        self._initExamList()
        self._initPaperList()

    def deletePapers(self):
        currentPaper = self.ui.paperList.currentItem()

        if not currentPaper:
            QMessageBox.warning(self, "警告", "请先选择一张试卷")
            logger.warning("请先选择一张试卷")
            return

        if currentPaper.parent():
            with Sql.getSession() as session:
                if paper := Sql.Papers.get(int(currentPaper.text(0)), session=session):
                    paper.delete(session=session)
        else:
            QMessageBox.warning(self, "警告", "请先选择一张试卷")
            logger.warning("请先选择一张试卷")

        logger.info(f"成功删除试卷: {currentPaper.text(1)}")

        self._initExamList()
        self._initPaperList()

    def checkChosed(self):
        if self.apiThread and self.apiThread.isRunning():
            reply = QMessageBox.question(
                self,
                "确认",
                "检查正在进行中，确定要取消当前操作吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.No:
                return
            self.apiThread.terminate()
            self.apiThread = None

        current = self.ui.paperList.currentItem()

        if not current:
            QMessageBox.warning(self, "警告", "请先选择一张试卷或考试")
            logger.warning("请先选择一张试卷或考试")
            return

        if current.parent():
            if paper := Sql.Papers.get(int(current.text(0))):
                papers = [paper]
                exam = Sql.Exam.get(paper.belong)
                if not exam:
                    QMessageBox.warning(self, "警告", "未找到对应的考试")
                    return
            else:
                QMessageBox.warning(self, "警告", "未找到对应的试卷")
                logger.warning("未找到对应的试卷")
                return
        else:
            exam = Sql.Exam.get(int(current.text(0)))
            if exam:
                papers = Sql.Papers.getByExamId(exam.id)
            else:
                QMessageBox.warning(self, "警告", "未找到对应的考试")
                logger.warning("未找到对应的考试")
                return

        tasks: list[DataTypes.Task] = []
        tasks.extend(
            DataTypes.Task(
                id=str(paper.id),
                examRemoteId=exam.remoteId,
                imgUrl=f"{self.cfUrl}/{paper.img}",
                imgPath=Paths.data / "imgs" / paper.img,
                apiReply=None,
            )
            for paper in papers
        )
        logger.info(f"选中的试卷: {len(papers)} 张")

        self.apiThread = SubThreads.CallApiThread(tasks)
        self.apiThread.allTasksFinished.connect(self._finishCkeck)
        self.apiThread.progress.connect(self._mamageCheckProgress)
        self.apiThread.start()

    def showPaerAndDetales(self):
        current = self.ui.paperList.currentItem()
        if current.parent():
            if paper := Sql.Papers.get(int(current.text(0))):
                showPaper = f"""
                    <html>
                        <body style="margin:0; padding:0;">
                            <img src="{(Paths.data / "imgs" / paper.img).as_uri()}" 
                                style="display: block; margin: 0 auto; max-width: 100%; height: auto;" />
                        </body>
                    </html>
                """
                self.ui.showPaper.setHtml(showPaper)

                if comment := paper.comment:
                    self.ui.showDetals.setHtml(
                        HandleApiResult.result2Html(
                            comment.data.result, self.showOption
                        )
                    )
                else:
                    self.ui.showDetals.setHtml(HandleApiResult.result2Html())

    def showOptionsChanged(self, options: Enums.ShowDetaleOption):
        logger.info(f"显示选项改变: {options}")

    def _initExamList(self):
        exams: list[Sql.Exam] = Sql.Exam.getAll()

        self.ui.examList.clear()
        for exam in exams:
            self.ui.examList.addItem(exam.name)

    def _initPaperList(self):
        exams: list[Sql.Exam] = Sql.Exam.getAll()
        papers: list[Sql.Papers] = Sql.Papers.getAll()

        examItems: list[QTreeWidgetItem] = []
        paperItems: list[QTreeWidgetItem] = []

        self.ui.paperList.clear()
        for exam in exams:
            examItem = QTreeWidgetItem([str(exam.id), exam.name])
            examItems.append(examItem)

        for paper in papers:
            paperItem = QTreeWidgetItem([str(paper.id), Path(paper.img).name])
            for examItem in examItems:
                if examItem.text(0) == str(paper.belong):
                    examItem.addChild(paperItem)
                    break
            paperItems.append(paperItem)

        self.ui.paperList.addTopLevelItems(examItems)

    def _initSubThreads(self):
        def getCfUrl(url: str):
            self.cfUrl = url

        def getAvailablePort(startPort: int = 8000, maxAttempts: int = 100) -> int:
            """从指定端口开始，获取第一个可用的端口"""
            for port in range(startPort, startPort + maxAttempts):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        s.bind(("localhost", port))
                        logger.info(f"找到可用端口：{port}")
                        return port
                except OSError:
                    logger.debug(f"端口 {port} 被占用")
                    continue

            raise OSError(
                f"无法在端口范围 {startPort}-{startPort + maxAttempts - 1} 内找到可用端口"
            )

        port = getAvailablePort()
        self.fileServer = SubThreads.FileServerThread(port=port)
        self.cloudflare = SubThreads.CloudflareThread(port=port, timeout=10)
        self.cloudflare.result.connect(getCfUrl)

        self.fileServer.start()
        self.cloudflare.start()

        logger.info(f"成功建立文件服务器：{self.cfUrl}")

    def _finishCkeck(self, tasks: list[DataTypes.Task]):
        QMessageBox.information(self, "提示", f"检查完成，共处理 {len(tasks)} 个任务")

    def _mamageCheckProgress(self, prog: int):
        self.ui.checkProgress.setValue(prog)
