# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 413)
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"border: none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: #F8F9FA;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 15px;\n"
"padding: 5px 15px;\n"
"background-color:  #F8F9FA;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #E9ECEF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:  #DEE2E6;\n"
"}\n"
"#header, #mainBody {\n"
"background-color: #DEE2E6;\n"
"}\n"
"\n"
"#title {\n"
"background: transparent;\n"
"color: #000000;\n"
"}\n"
"\n"
"QTableView {\n"
"background-color: #DEE2E6;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: #CED4DA;\n"
"height: 50px;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"background-color: #CED4DA;\n"
"boarder-style: none;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"color: #FFF;\n"
"background-color: #ADB5BD;\n"
"boarder: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 300))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, -1)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(25, 9, 20, 9)
        self.title = QLabel(self.header)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semilight"])
        font1.setPointSize(20)
        self.title.setFont(font1)

        self.horizontalLayout.addWidget(self.title)

        self.widget = QWidget(self.header)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.deleteBtn = QPushButton(self.widget)
        self.deleteBtn.setObjectName(u"deleteBtn")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semilight"])
        font2.setPointSize(14)
        self.deleteBtn.setFont(font2)
        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteBtn.setIconSize(QSize(25, 25))
        self.deleteBtn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.deleteBtn)

        self.editBtn = QPushButton(self.widget)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy)
        self.editBtn.setFont(font2)
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editBtn.setIconSize(QSize(25, 25))
        self.editBtn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.editBtn)

        self.newTaskBtn = QPushButton(self.widget)
        self.newTaskBtn.setObjectName(u"newTaskBtn")
        self.newTaskBtn.setFont(font2)
        self.newTaskBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newTaskBtn.setIconSize(QSize(25, 25))
        self.newTaskBtn.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.newTaskBtn)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.mainBody)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 0))
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(100)
        self.tableView.horizontalHeader().setDefaultSectionSize(100)
        self.tableView.horizontalHeader().setHighlightSections(True)
        self.tableView.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setDefaultSectionSize(24)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.tableView.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.tableView)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoshka", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"ToDoshka", None))
        self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.newTaskBtn.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
    # retranslateUi

