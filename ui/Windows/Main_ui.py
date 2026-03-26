# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 720)
        self.showOrHideLog = QAction(MainWindow)
        self.showOrHideLog.setObjectName(u"showOrHideLog")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.examTab = QWidget()
        self.examTab.setObjectName(u"examTab")
        self.gridLayout_4 = QGridLayout(self.examTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.examTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.examList = QListWidget(self.groupBox)
        self.examList.setObjectName(u"examList")

        self.gridLayout_2.addWidget(self.examList, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 2, 1)

        self.groupBox_2 = QGroupBox(self.examTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.examName = QLineEdit(self.groupBox_2)
        self.examName.setObjectName(u"examName")

        self.verticalLayout_2.addWidget(self.examName)

        self.examRemoteId = QLineEdit(self.groupBox_2)
        self.examRemoteId.setObjectName(u"examRemoteId")

        self.verticalLayout_2.addWidget(self.examRemoteId)

        self.paperCount = QLineEdit(self.groupBox_2)
        self.paperCount.setObjectName(u"paperCount")
        self.paperCount.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.paperCount)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.examTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.creatNewExam = QPushButton(self.groupBox_3)
        self.creatNewExam.setObjectName(u"creatNewExam")

        self.horizontalLayout_2.addWidget(self.creatNewExam)

        self.deleteExam = QPushButton(self.groupBox_3)
        self.deleteExam.setObjectName(u"deleteExam")

        self.horizontalLayout_2.addWidget(self.deleteExam)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.tabWidget.addTab(self.examTab, "")
        self.checkTab = QWidget()
        self.checkTab.setObjectName(u"checkTab")
        self.horizontalLayout_4 = QHBoxLayout(self.checkTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_4 = QGroupBox(self.checkTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.paperList = QTreeWidget(self.groupBox_4)
        self.paperList.setObjectName(u"paperList")

        self.gridLayout_5.addWidget(self.paperList, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.checkTab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.showPaper = QTextBrowser(self.groupBox_8)
        self.showPaper.setObjectName(u"showPaper")

        self.gridLayout_6.addWidget(self.showPaper, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.checkTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.importPapers = QPushButton(self.groupBox_6)
        self.importPapers.setObjectName(u"importPapers")

        self.verticalLayout_3.addWidget(self.importPapers)

        self.deleteChoosed = QPushButton(self.groupBox_6)
        self.deleteChoosed.setObjectName(u"deleteChoosed")

        self.verticalLayout_3.addWidget(self.deleteChoosed)


        self.horizontalLayout_3.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkExam = QPushButton(self.groupBox_7)
        self.checkExam.setObjectName(u"checkExam")

        self.verticalLayout_4.addWidget(self.checkExam)

        self.recheckChoosed = QPushButton(self.groupBox_7)
        self.recheckChoosed.setObjectName(u"recheckChoosed")

        self.verticalLayout_4.addWidget(self.recheckChoosed)


        self.horizontalLayout_3.addWidget(self.groupBox_7)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.groupBox_9 = QGroupBox(self.checkTab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.showScore = QLabel(self.groupBox_9)
        self.showScore.setObjectName(u"showScore")

        self.verticalLayout_6.addWidget(self.showScore)

        self.showDetals = QTextEdit(self.groupBox_9)
        self.showDetals.setObjectName(u"showDetals")
        self.showDetals.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.showDetals)


        self.horizontalLayout_4.addWidget(self.groupBox_9)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 5)
        self.tabWidget.addTab(self.checkTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.logBox = QDockWidget(MainWindow)
        self.logBox.setObjectName(u"logBox")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.showLog = QTextEdit(self.dockWidgetContents)
        self.showLog.setObjectName(u"showLog")
        self.showLog.setReadOnly(True)

        self.gridLayout_7.addWidget(self.showLog, 0, 0, 1, 1)

        self.logBox.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.logBox)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.showOrHideLog)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.showOrHideLog.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a/\u9690\u85cf \u65e5\u5fd7", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8003\u8bd5\u5217\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u7f16\u8f91", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8003\u8bd5\u540d\u79f0(\u9009\u586b)\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7f16\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bd5\u5377\u6570\u91cf\uff1a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.creatNewExam.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u8003\u8bd5", None))
        self.deleteExam.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8003\u8bd5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.examTab), QCoreApplication.translate("MainWindow", u"\u8003\u8bd5\u7ba1\u7406", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8003\u8bd5\u5217\u8868", None))
        ___qtreewidgetitem = self.paperList.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u9879\u76ee", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u8bd5\u5377\u9884\u89c8", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u8bd5\u5377\u64cd\u4f5c", None))
        self.importPapers.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u8bd5\u5377", None))
        self.deleteChoosed.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u5b9a", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u6279\u6539\u64cd\u4f5c", None))
        self.checkExam.setText(QCoreApplication.translate("MainWindow", u"\u6279\u6539\u8003\u8bd5", None))
        self.recheckChoosed.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u9605\u9009\u4e2d", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u8bc4\u8bed", None))
        self.showScore.setText(QCoreApplication.translate("MainWindow", u"\u5206\u6570\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.checkTab), QCoreApplication.translate("MainWindow", u"\u8bd5\u5377\u6279\u9605", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u4ef6\u7ba1\u7406", None))
        self.logBox.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u8f93\u51fa", None))
    # retranslateUi

