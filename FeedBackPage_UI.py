import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import src_images

class Ui_Feedback(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(710, 350)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: #fffefe;\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"border: 0px solid black;\n"
"border-radius:0px;")
        self.response_bar = QLineEdit(self.widget_2)
        self.response_bar.setObjectName(u"response_bar")
        self.response_bar.setGeometry(QRect(20, 210, 641, 49))
        font = QFont()
        font.setFamilies([u"League Spartan Medium"])
        font.setPointSize(16)
        self.response_bar.setFont(font)
        self.response_bar.setStyleSheet(u"QLineEdit{\n"
"border:2px solid #e5e6ea;\n"
"border-radius: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"padding: 10px;\n"
"}\n"
"")
        self.response_bar.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.bulb_image = QLabel(self.widget_2)
        self.bulb_image.setObjectName(u"bulb_image")
        self.bulb_image.setGeometry(QRect(270, 0, 151, 121))
        self.bulb_image.setStyleSheet(u"image: url(:/src/images/lightbulb.png);")
        self.Message = QLabel(self.widget_2)
        self.Message.setObjectName(u"Message")
        self.Message.setGeometry(QRect(40, 150, 611, 31))
        self.Message.setStyleSheet(u"font: 900 20pt \"League Spartan Black\";")
        self.submit_button = QPushButton(self.widget_2)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(610, 275, 51, 31))
        self.submit_button.setStyleSheet(u"QPushButton{\n"
"	border-radius: 10px;\n"
"	image: url(:/src/images/sumit.png);\n"
"	background: transparent;\n"
"	background-color: #f1f1f1;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"padding: 5px;\n"
"background-color: #c1c1c1;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Feedback", None))
        self.response_bar.setText("")
        self.bulb_image.setText("")
        self.Message.setText(QCoreApplication.translate("Dialog", u"Help us improve! Could you share your feedback?", None))
        self.submit_button.setText("")
    
