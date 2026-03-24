from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog, QMessageBox
from modules import logger, uiLogger, Sql
from pathlib import Path
from .Windows import Main_ui


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Main_ui.Ui_MainWindow()
        self.ui.setupUi(self)  # type: ignore
        uiLogger.log.connect(self.ui.showLog.append)

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
        self.ui.importPapers.clicked.connect(self.importPapers)
        self.ui.deleteChoosed.clicked.connect(self.deletePapers)

        self._initExamList()
        self._initPaperList()

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

    def createExam(self):
        Sql.Exam.create(
            name=self.ui.examName.text(),
            remoteId=self.ui.examRemoteId.text()
        )

        self._initExamList()
        self._initPaperList()

    def deleteExam(self):
        currentExam = self.ui.examList.currentItem()
        if currentExam:
            exam = Sql.Exam.get(currentExam.text())
            if exam:
                exam.delete()
                
        self._initExamList()
        self._initPaperList()

    def importPapers(self):
        currentExam = self.ui.paperList.currentItem()
        if not currentExam:
            QMessageBox.warning(self, "警告", "请先选择一个考试")
            return
        
        if currentExam.parent():
            examId = int(currentExam.parent().text(0))
        else:
            examId = int(currentExam.text(0))

        files, _ = QFileDialog.getOpenFileNames(self, "选取试卷图片", "", "图片 (*.png *.jpg *.jpeg)")
        for file in files:
            with Sql.getSession() as session:
                Sql.Papers.add(belong=examId, img=file, session=session)

        self._initExamList()
        self._initPaperList()

    def deletePapers(self):
        self._initExamList()
        self._initPaperList()