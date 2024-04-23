# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(227, 317)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setStyleSheet(u"* {\n"
"border: none;\n"
"background: #CED4DA;\n"
"padding: 0;\n"
"margin: 0;\n"
"}\n"
"\n"
"#dialog{\n"
"background-color: #F8F9FA;\n"
"}\n"
"\n"
"#header, #mainBody {\n"
"background-color: #DEE2E6;\n"
"}\n"
"\n"
"#title, QPlainTextEdit, QLineEdit, QLabel, QComboBox, QDateEdit {\n"
"background: transparent;\n"
"color: #000000;\n"
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
"}")
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.header = QWidget(dialog)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        self.header.setMinimumSize(QSize(100, 0))
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleEdit = QLineEdit(self.header)
        self.titleEdit.setObjectName(u"titleEdit")
        font = QFont()
        font.setFamilies([u"Segoe UI Semilight"])
        font.setPointSize(12)
        self.titleEdit.setFont(font)
        self.titleEdit.setMaxLength(20)
        self.titleEdit.setAlignment(Qt.AlignCenter)
        self.titleEdit.setDragEnabled(False)
        self.titleEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.titleEdit)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(dialog)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy2)
        self.mainBody.setMinimumSize(QSize(227, 252))
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.descriptionEdit = QPlainTextEdit(self.mainBody)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout_2.addWidget(self.descriptionEdit)

        self.deadline = QLabel(self.mainBody)
        self.deadline.setObjectName(u"deadline")
        font1 = QFont()
        font1.setItalic(True)
        self.deadline.setFont(font1)

        self.verticalLayout_2.addWidget(self.deadline)

        self.deadlineEdit = QDateEdit(self.mainBody)
        self.deadlineEdit.setObjectName(u"deadlineEdit")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semilight"])
        self.deadlineEdit.setFont(font2)
        self.deadlineEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.deadlineEdit.setDateTime(QDateTime(QDate(2024, 4, 14), QTime(21, 0, 0)))
        self.deadlineEdit.setMaximumDateTime(QDateTime(QDate(2100, 12, 31), QTime(20, 59, 59)))
        self.deadlineEdit.setCalendarPopup(True)
        self.deadlineEdit.setDate(QDate(2024, 4, 14))

        self.verticalLayout_2.addWidget(self.deadlineEdit)

        self.statusEdit = QComboBox(self.mainBody)
        self.statusEdit.addItem("")
        self.statusEdit.addItem("")
        self.statusEdit.addItem("")
        self.statusEdit.addItem("")
        self.statusEdit.setObjectName(u"statusEdit")
        self.statusEdit.setFont(font2)
        self.statusEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.statusEdit.setEditable(False)
        self.statusEdit.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_2.addWidget(self.statusEdit)

        self.completeBtn = QPushButton(self.mainBody)
        self.completeBtn.setObjectName(u"completeBtn")
        sizePolicy1.setHeightForWidth(self.completeBtn.sizePolicy().hasHeightForWidth())
        self.completeBtn.setSizePolicy(sizePolicy1)
        self.completeBtn.setFont(font)
        self.completeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.completeBtn, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.mainBody)


        self.retranslateUi(dialog)

        self.statusEdit.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Task Editor", None))
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"Task Title", None))
        self.descriptionEdit.setPlaceholderText(QCoreApplication.translate("dialog", u"Description", None))
        self.deadline.setText(QCoreApplication.translate("dialog", u"Deadline", None))
        self.statusEdit.setItemText(0, QCoreApplication.translate("dialog", u"Backlog", None))
        self.statusEdit.setItemText(1, QCoreApplication.translate("dialog", u"InProgress", None))
        self.statusEdit.setItemText(2, QCoreApplication.translate("dialog", u"Review", None))
        self.statusEdit.setItemText(3, QCoreApplication.translate("dialog", u"Done", None))

#if QT_CONFIG(tooltip)
        self.statusEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.statusEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.statusEdit.setCurrentText("")
        self.statusEdit.setProperty("placeholderText", QCoreApplication.translate("dialog", u"Choose status", None))
        self.completeBtn.setText(QCoreApplication.translate("dialog", u"Complete", None))
    # retranslateUi

