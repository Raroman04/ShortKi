import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import src_images

class Ui_CreateAcc(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/src/icons/keycap.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.widget_4.setGeometry(QRect(50, 440, 321, 141))
        self.registerbutton = QPushButton(self.widget_4)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setGeometry(QRect(20, 10, 275, 40))
        self.registerbutton.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"font: 800 15pt \"League Spartan ExtraBold\";\n"
"border-radius: 20px;\n"
"background-color: rgb(251, 168, 97);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(252, 158, 87);\n"
"	border: 2px solid #f1f1f1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(252, 148, 77);    \n"
"}")
        self.Goback_button = QPushButton(self.widget_4)
        self.Goback_button.setObjectName(u"Goback_button")
        self.Goback_button.setGeometry(QRect(20, 70, 275, 40))
        self.Goback_button.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"font: 800 15pt \"League Spartan ExtraBold\";\n"
"border-radius: 20px;\n"
"background-color: rgb(153, 214, 222);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(143, 204, 212);\n"
"	border: 2px solid #f1f1f1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(123, 184, 192);    \n"
"}")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(50, 170, 321, 241))
        self.frame_password = QFrame(self.widget_3)
        self.frame_password.setObjectName(u"frame_password")
        self.frame_password.setGeometry(QRect(20, 100, 275, 51))
        self.frame_password.setStyleSheet(u"border: 3px solid black;\n"
"border-radius: 20px;")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.password_image = QLabel(self.frame_password)
        self.password_image.setObjectName(u"password_image")
        self.password_image.setGeometry(QRect(10, 10, 31, 31))
        self.password_image.setStyleSheet(u"border: 0px;")
        self.password_image.setPixmap(QPixmap(u":/src/icons/square-asterisk.png"))
        self.password_image.setScaledContents(True)
        self.enter_password = QLineEdit(self.frame_password)
        self.enter_password.setObjectName(u"enter_password")
        self.enter_password.setGeometry(QRect(50, 11, 211, 31))
        self.enter_password.setStyleSheet(u"border: 0px;\n"
"font: 15pt \"League Spartan\";")
        self.enter_password.setEchoMode(QLineEdit.Password)
        self.username_frame = QFrame(self.widget_3)
        self.username_frame.setObjectName(u"username_frame")
        self.username_frame.setGeometry(QRect(20, 20, 275, 51))
        self.username_frame.setStyleSheet(u"QFrame{\n"
"border: 3px solid black;\n"
"border-radius: 20px;\n"
"}")
        self.username_frame.setFrameShape(QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QFrame.Raised)
        self.username_image = QLabel(self.username_frame)
        self.username_image.setObjectName(u"username_image")
        self.username_image.setGeometry(QRect(10, 10, 31, 31))
        self.username_image.setStyleSheet(u"border: 0px;")
        self.username_image.setPixmap(QPixmap(u":/src/icons/user-round.png"))
        self.username_image.setScaledContents(True)
        self.enter_username = QLineEdit(self.username_frame)
        self.enter_username.setObjectName(u"enter_username")
        self.enter_username.setGeometry(QRect(50, 11, 211, 31))
        self.enter_username.setStyleSheet(u"border: 0px;\n"
"font: 15pt \"League Spartan\";")
        self.frame_confirmpass = QFrame(self.widget_3)
        self.frame_confirmpass.setObjectName(u"frame_confirmpass")
        self.frame_confirmpass.setGeometry(QRect(20, 180, 275, 51))
        self.frame_confirmpass.setStyleSheet(u"border: 3px solid black;\n"
"border-radius: 20px;")
        self.frame_confirmpass.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmpass.setFrameShadow(QFrame.Raised)
        self.confirmpass_image = QLabel(self.frame_confirmpass)
        self.confirmpass_image.setObjectName(u"confirmpass_image")
        self.confirmpass_image.setGeometry(QRect(10, 10, 31, 31))
        self.confirmpass_image.setStyleSheet(u"border: 0px;")
        self.confirmpass_image.setPixmap(QPixmap(u":/src/icons/square-asterisk.png"))
        self.confirmpass_image.setScaledContents(True)
        self.enter_confirmpass = QLineEdit(self.frame_confirmpass)
        self.enter_confirmpass.setObjectName(u"enter_confirmpass")
        self.enter_confirmpass.setGeometry(QRect(50, 11, 211, 31))
        self.enter_confirmpass.setStyleSheet(u"border: 0px;\n"
"font: 15pt \"League Spartan\";")
        self.enter_confirmpass.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(153, 214, 222);\n"
"border-right: 3px solid black;")
        self.ShortKi_title = QLabel(self.widget)
        self.ShortKi_title.setObjectName(u"ShortKi_title")
        self.ShortKi_title.setGeometry(QRect(120, 180, 141, 41))
        self.ShortKi_title.setStyleSheet(u"background: transparent;\n"
"border: 0px;\n"
"font: 800 30pt \"League Spartan ExtraBold\";")
        self.keyboard_image = QLabel(self.widget)
        self.keyboard_image.setObjectName(u"keyboard_image")
        self.keyboard_image.setGeometry(QRect(90, 250, 211, 141))
        self.keyboard_image.setStyleSheet(u"border: 0px;")
        self.keyboard_image.setPixmap(QPixmap(u":/src/images/keyboardimage.png"))
        self.keyboard_image.setScaledContents(True)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ShortKi", None))
        self.Welcome_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">WELCOME</p></body></html>", None))
        self.registerbutton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.Goback_button.setText(QCoreApplication.translate("MainWindow", u"Go back", None))
        self.password_image.setText("")
        self.enter_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.username_image.setText("")
        self.enter_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.confirmpass_image.setText("")
        self.enter_confirmpass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.ShortKi_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ShortKi</p></body></html>", None))
        self.keyboard_image.setText("")
    # retranslateUi


