import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import src_images

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"border-radius: 10px;\n"
"background-color: rgb(153, 214, 222);\n"
"}")
        self.Keyboard_image = QLabel(self.widget)
        self.Keyboard_image.setObjectName(u"Keyboard_image")
        self.Keyboard_image.setGeometry(QRect(200, 170, 241, 171))
        self.Keyboard_image.setStyleSheet(u"border: 0px;")
        self.Keyboard_image.setPixmap(QPixmap(u":/src/images/keyboardimage.png"))
        self.Keyboard_image.setScaledContents(True)
        self.ShortKi_Title = QLabel(self.widget)
        self.ShortKi_Title.setObjectName(u"ShortKi_Title")
        self.ShortKi_Title.setGeometry(QRect(220, 80, 191, 41))
        self.ShortKi_Title.setStyleSheet(u"background: transparent;\n"
"border: 0px;\n"
"font: 800 40pt \"League Spartan ExtraBold\";")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(145, 400, 350, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: #fffefe;\n"
"border: 0px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"background-color: rgb(242, 109, 125);\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Keyboard_image.setText("")
        self.ShortKi_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ShortKi</p></body></html>", None))
    # retranslateUi
