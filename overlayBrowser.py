import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import oldsrc

class Ui_Browser(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 700)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(1270, 50))
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 10, 651, 32))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(2000, 16777215))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setStyleSheet(u"font: 800 30pt \"League Spartan ExtraBold\";\n"
"image: url(:/src/Screenshot 2024-04-11 023215.png);\n"
"border: 0px;")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 0, 51, 50))
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(500, 50))
        self.label_3.setStyleSheet(u"image: url(:/src/images/web browser.png);\n"
"border: 0px;\n"
"")

        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(1273, 800))
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(288, 251))
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_46 = QPushButton(self.widget_5)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setMinimumSize(QSize(0, 0))
        self.pushButton_46.setMaximumSize(QSize(271, 191))
        self.pushButton_46.setAutoFillBackground(False)
        self.pushButton_46.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/recently closed tab.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.pushButton_46, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(270, 36))
        self.label_2.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022517.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(288, 251))
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_47 = QPushButton(self.widget_4)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(0, 0))
        self.pushButton_47.setMaximumSize(QSize(271, 191))
        self.pushButton_47.setAutoFillBackground(False)
        self.pushButton_47.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Open new tab.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_47, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(270, 36))
        self.label_4.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022816.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(288, 251))
        self.gridLayout_5 = QGridLayout(self.widget_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_48 = QPushButton(self.widget_6)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setMinimumSize(QSize(0, 0))
        self.pushButton_48.setMaximumSize(QSize(271, 191))
        self.pushButton_48.setAutoFillBackground(False)
        self.pushButton_48.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Close current tab.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_48, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(270, 36))
        self.label_5.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022258.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(288, 251))
        self.gridLayout_10 = QGridLayout(self.widget_11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_52 = QPushButton(self.widget_11)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(0, 0))
        self.pushButton_52.setMaximumSize(QSize(271, 191))
        self.pushButton_52.setAutoFillBackground(False)
        self.pushButton_52.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Open downloads.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.pushButton_52, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(270, 36))
        self.label_6.setStyleSheet(u"border: 0px;\n"
"font: 900 18pt \"League Spartan Black\";\n"
"image: url(:/src/Screenshot 2024-04-11 022511.png);")

        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_11, 0, 3, 1, 1)

        self.Line1AllWidget = QFrame(self.widget_3)
        self.Line1AllWidget.setObjectName(u"Line1AllWidget")
        self.Line1AllWidget.setStyleSheet(u"background-color: rgba(0,0,0,45);\n"
"")
        self.Line1AllWidget.setFrameShape(QFrame.HLine)
        self.Line1AllWidget.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.Line1AllWidget, 1, 0, 1, 4)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(300, 251))
        self.gridLayout_6 = QGridLayout(self.widget_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_49 = QPushButton(self.widget_7)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMinimumSize(QSize(0, 0))
        self.pushButton_49.setMaximumSize(QSize(271, 191))
        self.pushButton_49.setAutoFillBackground(False)
        self.pushButton_49.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Open bookmark manager.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.pushButton_49, 0, 0, 1, 1)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(280, 36))
        self.label_7.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022608.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_7, 2, 0, 1, 1)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(288, 251))
        self.gridLayout_7 = QGridLayout(self.widget_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_50 = QPushButton(self.widget_8)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setMinimumSize(QSize(0, 0))
        self.pushButton_50.setMaximumSize(QSize(271, 191))
        self.pushButton_50.setAutoFillBackground(False)
        self.pushButton_50.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Find text.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.pushButton_50, 0, 0, 1, 1)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(270, 36))
        self.label_8.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022523.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_8, 2, 1, 1, 1)

        self.widget_9 = QWidget(self.widget_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.widget_9.setMaximumSize(QSize(288, 251))
        self.gridLayout_8 = QGridLayout(self.widget_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_51 = QPushButton(self.widget_9)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setMinimumSize(QSize(0, 0))
        self.pushButton_51.setMaximumSize(QSize(271, 191))
        self.pushButton_51.setAutoFillBackground(False)
        self.pushButton_51.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/Jump to address bar.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"\n"
"")

        self.gridLayout_8.addWidget(self.pushButton_51, 0, 0, 1, 1)

        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(270, 36))
        self.label_9.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022528.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_8.addWidget(self.label_9, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_9, 2, 2, 1, 1)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.widget_10.setMaximumSize(QSize(288, 251))
        self.gridLayout_9 = QGridLayout(self.widget_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_53 = QPushButton(self.widget_10)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setMinimumSize(QSize(0, 0))
        self.pushButton_53.setMaximumSize(QSize(271, 191))
        self.pushButton_53.setAutoFillBackground(False)
        self.pushButton_53.setStyleSheet(u"QPushButton{\n"
"	image: url(:/src/images/jump to previous tab.png);\n"
"background-color: rgb(242, 242, 244);\n"
"border-radius: 9px;\n"
"border: 0px;\n"
"}\n"
"")

        self.gridLayout_9.addWidget(self.pushButton_53, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(270, 36))
        self.label_10.setStyleSheet(u"border: 0px;\n"
"image: url(:/src/Screenshot 2024-04-11 022534.png);\n"
"font: 900 18pt \"League Spartan Black\";")

        self.gridLayout_9.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_10, 2, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_3.setText("")
        self.pushButton_46.setText("")
        self.label_2.setText("")
        self.pushButton_47.setText("")
        self.label_4.setText("")
        self.pushButton_48.setText("")
        self.label_5.setText("")
        self.pushButton_52.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'League Spartan Black'; font-size:18pt; font-weight:900; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_49.setText("")
        self.label_7.setText("")
        self.pushButton_50.setText("")
        self.label_8.setText("")
        self.pushButton_51.setText("")
        self.label_9.setText("")
        self.pushButton_53.setText("")
        self.label_10.setText("")
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Browser()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



