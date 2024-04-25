import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import src_images

class Ui_Login(object):
    def setupUi(self, ShortKi):
        if not ShortKi.objectName():
            ShortKi.setObjectName(u"ShortKi")
        ShortKi.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/src/icons/keycap.ico", QSize(), QIcon.Normal, QIcon.Off)
        ShortKi.setWindowIcon(icon)
        self.centralwidget = QWidget(ShortKi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(153, 214, 222);\n"
"border-right: 3px solid black;")
        self.ShortKi_Title = QLabel(self.widget)
        self.ShortKi_Title.setObjectName(u"ShortKi_Title")
        self.ShortKi_Title.setGeometry(QRect(120, 180, 141, 41))
        self.ShortKi_Title.setStyleSheet(u"background: transparent;\n"
"border: 0px;\n"
"font: 800 30pt \"League Spartan ExtraBold\";")
        self.Keyboard_image = QLabel(self.widget)
        self.Keyboard_image.setObjectName(u"Keyboard_image")
        self.Keyboard_image.setGeometry(QRect(90, 250, 211, 141))
        self.Keyboard_image.setStyleSheet(u"border: 0px;")
        self.Keyboard_image.setPixmap(QPixmap(u":/src/images/keyboardimage.png"))
        self.Keyboard_image.setScaledContents(True)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.Welcome_title = QLabel(self.widget_2)
        self.Welcome_title.setObjectName(u"Welcome_title")
        self.Welcome_title.setGeometry(QRect(120, 90, 161, 41))
        self.Welcome_title.setStyleSheet(u"border: 0px;\n"
"font: 800 25pt \"League Spartan ExtraBold\";")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(50, 400, 321, 141))
        self.LoginButton = QPushButton(self.widget_4)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(20, 20, 275, 40))
        self.LoginButton.setStyleSheet(u"QPushButton {\n"
"border: 0px;\n"
"font: 800 15pt \"League Spartan ExtraBold\";\n"
"border-radius: 20px;\n"
"background-color: rgb(242, 109, 125);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(232, 99, 115);\n"
"	border: 2px solid #f1f1f1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(202, 69, 95);    \n"
"\n"
"}\n"
"\n"
"")
        self.CreateButton = QPushButton(self.widget_4)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setGeometry(QRect(20, 90, 275, 40))
        self.CreateButton.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"font: 800 15pt \"League Spartan ExtraBold\";\n"
"border-radius: 20px;\n"
"background-color: rgb(251, 168, 97);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(241, 158, 87);\n"
"	border: 2px solid #f1f1f1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(221, 128, 57);    \n"
"}")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(50, 190, 301, 161))
        self.frame_password = QFrame(self.widget_3)
        self.frame_password.setObjectName(u"frame_password")
        self.frame_password.setGeometry(QRect(20, 10, 275, 51))
        self.frame_password.setStyleSheet(u"border: 3px solid black;\n"
"border-radius: 20px;")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.Enter_Username = QLineEdit(self.frame_password)
        self.Enter_Username.setObjectName(u"Enter_Username")
        self.Enter_Username.setGeometry(QRect(50, 11, 211, 31))
        self.Enter_Username.setStyleSheet(u"border: 0px;\n"
"font: 15pt \"League Spartan\";")
        self.Enter_Username.setEchoMode(QLineEdit.Normal)
        self.user_image = QLabel(self.frame_password)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setGeometry(QRect(10, 10, 31, 31))
        self.user_image.setStyleSheet(u"border: 0px;")
        self.user_image.setPixmap(QPixmap(u":/src/icons/user-round.png"))
        self.user_image.setScaledContents(True)
        self.frame_username = QFrame(self.widget_3)
        self.frame_username.setObjectName(u"frame_username")
        self.frame_username.setGeometry(QRect(20, 90, 275, 51))
        self.frame_username.setStyleSheet(u"QFrame{\n"
"border: 3px solid black;\n"
"border-radius: 20px;\n"
"}")
        self.frame_username.setFrameShape(QFrame.StyledPanel)
        self.frame_username.setFrameShadow(QFrame.Raised)
        self.Enter_Password = QLineEdit(self.frame_username)
        self.Enter_Password.setObjectName(u"Enter_Password")
        self.Enter_Password.setGeometry(QRect(50, 11, 211, 31))
        self.Enter_Password.setStyleSheet(u"border: 0px;\n"
"font: 15pt \"League Spartan\";")
        self.Enter_Password.setEchoMode(QLineEdit.Password)
        self.password_image = QLabel(self.frame_username)
        self.password_image.setObjectName(u"password_image")
        self.password_image.setGeometry(QRect(10, 10, 31, 31))
        self.password_image.setStyleSheet(u"border: 0px;")
        self.password_image.setPixmap(QPixmap(u":/src/icons/square-asterisk.png"))
        self.password_image.setScaledContents(True)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        ShortKi.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShortKi)

        QMetaObject.connectSlotsByName(ShortKi)
    # setupUi

    def retranslateUi(self, ShortKi):
        ShortKi.setWindowTitle(QCoreApplication.translate("ShortKi", u"ShortKi", None))
        self.ShortKi_Title.setText(QCoreApplication.translate("ShortKi", u"<html><head/><body><p align=\"center\">ShortKi</p></body></html>", None))
        self.Keyboard_image.setText("")
        self.Welcome_title.setText(QCoreApplication.translate("ShortKi", u"<html><head/><body><p align=\"center\">WELCOME</p></body></html>", None))
        self.LoginButton.setText(QCoreApplication.translate("ShortKi", u"Login", None))
        self.LoginButton.setProperty("QPushButton:hover", "")
        self.CreateButton.setText(QCoreApplication.translate("ShortKi", u"Create Account", None))
        self.Enter_Username.setText("")
        self.Enter_Username.setPlaceholderText(QCoreApplication.translate("ShortKi", u"Username", None))
        self.user_image.setText("")
        self.Enter_Password.setPlaceholderText(QCoreApplication.translate("ShortKi", u"Password", None))
        self.password_image.setText("")
    # retranslateUi

