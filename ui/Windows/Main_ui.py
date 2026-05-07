# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QDockWidget,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QTextBrowser,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 720)
        self.showOrHideLog = QAction(MainWindow)
        self.showOrHideLog.setObjectName("showOrHideLog")
        self.showDetaleAll = QAction(MainWindow)
        self.showDetaleAll.setObjectName("showDetaleAll")
        self.showDetaleSelect = QAction(MainWindow)
        self.showDetaleSelect.setObjectName("showDetaleSelect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.examTab = QWidget()
        self.examTab.setObjectName("examTab")
        self.gridLayout_4 = QGridLayout(self.examTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QGroupBox(self.examTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.creatNewExam = QPushButton(self.groupBox_3)
        self.creatNewExam.setObjectName("creatNewExam")

        self.horizontalLayout_2.addWidget(self.creatNewExam)

        self.deleteExam = QPushButton(self.groupBox_3)
        self.deleteExam.setObjectName("deleteExam")

        self.horizontalLayout_2.addWidget(self.deleteExam)

        self.gridLayout_4.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.examTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.examName = QLineEdit(self.groupBox_2)
        self.examName.setObjectName("examName")

        self.verticalLayout_2.addWidget(self.examName)

        self.examRemoteId = QLineEdit(self.groupBox_2)
        self.examRemoteId.setObjectName("examRemoteId")

        self.verticalLayout_2.addWidget(self.examRemoteId)

        self.paperCount = QLineEdit(self.groupBox_2)
        self.paperCount.setObjectName("paperCount")
        self.paperCount.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.paperCount)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.examTab)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_8 = QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_4 = QLabel(self.groupBox_10)
        self.label_4.setObjectName("label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setOpenExternalLinks(True)

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.groupBox_10, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.examTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.examList = QListWidget(self.groupBox)
        self.examList.setObjectName("examList")

        self.gridLayout_2.addWidget(self.examList, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 3, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.tabWidget.addTab(self.examTab, "")
        self.checkTab = QWidget()
        self.checkTab.setObjectName("checkTab")
        self.horizontalLayout_4 = QHBoxLayout(self.checkTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_4 = QGroupBox(self.checkTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.paperList = QTreeWidget(self.groupBox_4)
        self.paperList.setObjectName("paperList")

        self.gridLayout_5.addWidget(self.paperList, 0, 0, 1, 1)

        self.horizontalLayout_4.addWidget(self.groupBox_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_8 = QGroupBox(self.checkTab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.showPaper = QTextBrowser(self.groupBox_8)
        self.showPaper.setObjectName("showPaper")

        self.gridLayout_6.addWidget(self.showPaper, 0, 0, 1, 1)

        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.checkTab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.importPapers = QPushButton(self.groupBox_6)
        self.importPapers.setObjectName("importPapers")

        self.verticalLayout_3.addWidget(self.importPapers)

        self.deleteChoosed = QPushButton(self.groupBox_6)
        self.deleteChoosed.setObjectName("deleteChoosed")

        self.verticalLayout_3.addWidget(self.deleteChoosed)

        self.horizontalLayout_3.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkChosed = QPushButton(self.groupBox_7)
        self.checkChosed.setObjectName("checkChosed")

        self.verticalLayout_4.addWidget(self.checkChosed)

        self.checkProgress = QProgressBar(self.groupBox_7)
        self.checkProgress.setObjectName("checkProgress")
        self.checkProgress.setValue(0)

        self.verticalLayout_4.addWidget(self.checkProgress)

        self.horizontalLayout_3.addWidget(self.groupBox_7)

        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.verticalLayout_5.setStretch(0, 5)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.groupBox_9 = QGroupBox(self.checkTab)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.showDetals = QWebEngineView(self.groupBox_9)
        self.showDetals.setObjectName("showDetals")
        self.showDetals.setUrl(QUrl("about:blank"))

        self.verticalLayout_6.addWidget(self.showDetals)

        self.horizontalLayout_4.addWidget(self.groupBox_9)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 5)
        self.tabWidget.addTab(self.checkTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1050, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.logBox = QDockWidget(MainWindow)
        self.logBox.setObjectName("logBox")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.showLog = QTextEdit(self.dockWidgetContents)
        self.showLog.setObjectName("showLog")
        self.showLog.setReadOnly(True)

        self.gridLayout_7.addWidget(self.showLog, 0, 0, 1, 1)

        self.logBox.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.logBox)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.showOrHideLog)
        self.menu_2.addAction(self.showDetaleAll)
        self.menu_2.addAction(self.showDetaleSelect)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.showOrHideLog.setText(
            QCoreApplication.translate(
                "MainWindow", "\u663e\u793a/\u9690\u85cf \u65e5\u5fd7", None
            )
        )
        self.showDetaleAll.setText(
            QCoreApplication.translate("MainWindow", "\u5168\u90e8", None)
        )
        self.showDetaleSelect.setText(
            QCoreApplication.translate("MainWindow", "\u624b\u52a8\u8c03\u6574", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("MainWindow", "\u64cd\u4f5c", None)
        )
        self.creatNewExam.setText(
            QCoreApplication.translate("MainWindow", "\u65b0\u5efa\u8003\u8bd5", None)
        )
        self.deleteExam.setText(
            QCoreApplication.translate("MainWindow", "\u5220\u9664\u8003\u8bd5", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "\u4fe1\u606f\u7f16\u8f91", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u8003\u8bd5\u540d\u79f0(\u9009\u586b)\uff1a", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "\u4efb\u52a1\u7f16\u53f7\uff1a", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow", "\u8bd5\u5377\u6570\u91cf\uff1a", None
            )
        )
        self.groupBox_10.setTitle(
            QCoreApplication.translate("MainWindow", "\u521b\u5efa\u4efb\u52a1", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                '\u8bf7\u524d\u5f80 <a href="https://api.extreme-code.cn/apply/dhxx/index.php">https://api.extreme-code.cn/apply/dhxx/index.php</a> \u8bbe\u7f6e\u8003\u8bd5\u4fe1\u606f\uff0c\u5e76\u590d\u5236\u8fd4\u56de\u7f16\u53f7',
                None,
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "\u8003\u8bd5\u5217\u8868", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.examTab),
            QCoreApplication.translate("MainWindow", "\u8003\u8bd5\u7ba1\u7406", None),
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate("MainWindow", "\u8003\u8bd5\u5217\u8868", None)
        )
        ___qtreewidgetitem = self.paperList.headerItem()
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("MainWindow", "\u9879\u76ee", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "\u7f16\u53f7", None)
        )
        self.groupBox_8.setTitle(
            QCoreApplication.translate("MainWindow", "\u8bd5\u5377\u9884\u89c8", None)
        )
        self.groupBox_5.setTitle(
            QCoreApplication.translate("MainWindow", "\u64cd\u4f5c", None)
        )
        self.groupBox_6.setTitle(
            QCoreApplication.translate("MainWindow", "\u8bd5\u5377\u64cd\u4f5c", None)
        )
        self.importPapers.setText(
            QCoreApplication.translate("MainWindow", "\u5bfc\u5165\u8bd5\u5377", None)
        )
        self.deleteChoosed.setText(
            QCoreApplication.translate("MainWindow", "\u5220\u9664\u9009\u5b9a", None)
        )
        self.groupBox_7.setTitle(
            QCoreApplication.translate("MainWindow", "\u6279\u6539\u64cd\u4f5c", None)
        )
        self.checkChosed.setText(
            QCoreApplication.translate("MainWindow", "\u6279\u6539\u9009\u4e2d", None)
        )
        self.groupBox_9.setTitle(
            QCoreApplication.translate("MainWindow", "\u8bc4\u8bed", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.checkTab),
            QCoreApplication.translate("MainWindow", "\u8bd5\u5377\u6279\u9605", None),
        )
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", "\u63a7\u4ef6\u7ba1\u7406", None)
        )
        self.menu_2.setTitle(
            QCoreApplication.translate("MainWindow", "\u663e\u793a\u9009\u9879", None)
        )
        self.logBox.setWindowTitle(
            QCoreApplication.translate("MainWindow", "\u65e5\u5fd7\u8f93\u51fa", None)
        )

    # retranslateUi
