# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"#main{\n"
"background-color: #0B132B\n"
"}\n"
"#mainBody, #header,#editPanel{\n"
"background-color:#3A506B\n"
"}\n"
"#taskList{\n"
"background-color:#1C2541;\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit, QTextEdit, #addTaskButton, #deadline, #createTask{\n"
"background-color: #1C2541;\n"
"padding: 5 px 5 px;\n"
"border-radius: 10px;\n"
"}\n"
"#deadlineDate{\n"
"padding: 5 px 5 px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.header = QWidget(self.main)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 9, 15, 9)
        self.Tittle = QLabel(self.header)
        self.Tittle.setObjectName(u"Tittle")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.Tittle.setFont(font)

        self.horizontalLayout.addWidget(self.Tittle, 0, Qt.AlignLeft)

        self.createTask = QWidget(self.header)
        self.createTask.setObjectName(u"createTask")
        self.createTask.setMinimumSize(QSize(150, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.createTask)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createButton = QPushButton(self.createTask)
        self.createButton.setObjectName(u"createButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.createButton.sizePolicy().hasHeightForWidth())
        self.createButton.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.createButton.setFont(font1)
        self.createButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"Icons/Add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createButton.setIcon(icon)
        self.createButton.setIconSize(QSize(20, 20))
        self.createButton.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.createButton)


        self.horizontalLayout.addWidget(self.createTask, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.main)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.taskList = QWidget(self.mainBody)
        self.taskList.setObjectName(u"taskList")
        sizePolicy.setHeightForWidth(self.taskList.sizePolicy().hasHeightForWidth())
        self.taskList.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.taskList)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget_2 = QStackedWidget(self.taskList)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2Page1 = QWidget()
        self.stackedWidget_2Page1.setObjectName(u"stackedWidget_2Page1")
        self.verticalLayout_5 = QVBoxLayout(self.stackedWidget_2Page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.stackedWidget_2Page1)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.stackedWidget_2.addWidget(self.stackedWidget_2Page1)

        self.verticalLayout_3.addWidget(self.stackedWidget_2)


        self.horizontalLayout_3.addWidget(self.taskList)

        self.editPanel = QWidget(self.mainBody)
        self.editPanel.setObjectName(u"editPanel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.editPanel.sizePolicy().hasHeightForWidth())
        self.editPanel.setSizePolicy(sizePolicy3)
        self.editPanel.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.editPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.editTitle = QWidget(self.editPanel)
        self.editTitle.setObjectName(u"editTitle")
        self.horizontalLayout_4 = QHBoxLayout(self.editTitle)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.titleIcon = QLabel(self.editTitle)
        self.titleIcon.setObjectName(u"titleIcon")
        sizePolicy1.setHeightForWidth(self.titleIcon.sizePolicy().hasHeightForWidth())
        self.titleIcon.setSizePolicy(sizePolicy1)
        self.titleIcon.setMinimumSize(QSize(40, 40))
        self.titleIcon.setMaximumSize(QSize(40, 40))
        self.titleIcon.setLayoutDirection(Qt.LeftToRight)
        self.titleIcon.setTextFormat(Qt.AutoText)
        self.titleIcon.setPixmap(QPixmap(u"Icons/EditTask.png"))
        self.titleIcon.setScaledContents(True)
        self.titleIcon.setOpenExternalLinks(False)

        self.horizontalLayout_4.addWidget(self.titleIcon)


        self.verticalLayout_2.addWidget(self.editTitle, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.properties = QWidget(self.editPanel)
        self.properties.setObjectName(u"properties")
        sizePolicy1.setHeightForWidth(self.properties.sizePolicy().hasHeightForWidth())
        self.properties.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.properties)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.titleEdit = QLineEdit(self.properties)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setMaxLength(20)
        self.titleEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.titleEdit, 0, Qt.AlignTop)

        self.descriptionEdit = QTextEdit(self.properties)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout_4.addWidget(self.descriptionEdit)

        self.deadline = QWidget(self.properties)
        self.deadline.setObjectName(u"deadline")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.deadline.sizePolicy().hasHeightForWidth())
        self.deadline.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.deadline)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, 3)
        self.deadlineText = QLabel(self.deadline)
        self.deadlineText.setObjectName(u"deadlineText")
        font2 = QFont()
        font2.setBold(True)
        self.deadlineText.setFont(font2)
        self.deadlineText.setLayoutDirection(Qt.LeftToRight)
        self.deadlineText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.deadlineText)

        self.deadlineDate = QDateEdit(self.deadline)
        self.deadlineDate.setObjectName(u"deadlineDate")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.deadlineDate.sizePolicy().hasHeightForWidth())
        self.deadlineDate.setSizePolicy(sizePolicy5)
        self.deadlineDate.setLayoutDirection(Qt.LeftToRight)
        self.deadlineDate.setAutoFillBackground(False)
        self.deadlineDate.setStyleSheet(u"")
        self.deadlineDate.setWrapping(False)
        self.deadlineDate.setFrame(False)
        self.deadlineDate.setReadOnly(False)
        self.deadlineDate.setKeyboardTracking(False)
        self.deadlineDate.setDateTime(QDateTime(QDate(2024, 3, 23), QTime(4, 0, 0)))
        self.deadlineDate.setCalendarPopup(True)
        self.deadlineDate.setDate(QDate(2024, 3, 23))

        self.horizontalLayout_5.addWidget(self.deadlineDate)


        self.verticalLayout_4.addWidget(self.deadline)

        self.addTaskButton = QPushButton(self.properties)
        self.addTaskButton.setObjectName(u"addTaskButton")
        sizePolicy.setHeightForWidth(self.addTaskButton.sizePolicy().hasHeightForWidth())
        self.addTaskButton.setSizePolicy(sizePolicy)
        self.addTaskButton.setMinimumSize(QSize(90, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.addTaskButton.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u"Icons/Plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addTaskButton.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.addTaskButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.properties)


        self.horizontalLayout_3.addWidget(self.editPanel)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoshka", None))
        self.Tittle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ToDoshka - Let's do it!</span></p></body></html>", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u" Create task!", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Deadline", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.titleIcon.setText("")
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.descriptionEdit.setDocumentTitle("")
        self.descriptionEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.deadlineText.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.addTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add task", None))
    # retranslateUi

