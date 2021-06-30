from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Sell(object):
    def setupUi(self, Sell):
        Sell.setObjectName("Sell")
        Sell.resize(940, 622)
        self.label = QtWidgets.QLabel(Sell)
        self.label.setGeometry(QtCore.QRect(480, 110, 111, 41))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.ticketnum = QtWidgets.QSpinBox(Sell)
        self.ticketnum.setGeometry(QtCore.QRect(610, 180, 51, 31))
        self.ticketnum.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.ticketnum.setMinimum(1)
        self.ticketnum.setObjectName("ticketnum")
        self.label_2 = QtWidgets.QLabel(Sell)
        self.label_2.setGeometry(QtCore.QRect(480, 180, 111, 31))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.credit = QtWidgets.QTextEdit(Sell)
        self.credit.setGeometry(QtCore.QRect(610, 110, 261, 41))
        self.credit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.credit.setObjectName("credit")
        self.label_3 = QtWidgets.QLabel(Sell)
        self.label_3.setGeometry(QtCore.QRect(480, 250, 111, 31))
        self.label_3.setStyleSheet("font: 14pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.sum = QtWidgets.QTextEdit(Sell)
        self.sum.setGeometry(QtCore.QRect(610, 250, 141, 41))
        self.sum.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.sum.setObjectName("sum")
        self.label_4 = QtWidgets.QLabel(Sell)
        self.label_4.setGeometry(QtCore.QRect(760, 260, 51, 31))
        self.label_4.setStyleSheet("font: 14pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.print = QtWidgets.QPushButton(Sell)
        self.print.setGeometry(QtCore.QRect(480, 410, 191, 51))
        self.print.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 16pt \"楷体\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";\n"
"}")
        self.print.setObjectName("print")
        self.execbtn = QtWidgets.QPushButton(Sell)
        self.execbtn.setGeometry(QtCore.QRect(700, 410, 201, 51))
        self.execbtn.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 16pt \"楷体\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 16pt \"楷体\";\n"
"}")
        self.execbtn.setObjectName("execbtn")
        self.widget = QtWidgets.QWidget(Sell)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 621))
        self.widget.setStyleSheet("border-image: url(./bg7.jpg);")
        self.widget.setObjectName("widget")

        self.retranslateUi(Sell)
        self.print.clicked.connect(Sell.printticket)
        self.execbtn.clicked.connect(Sell.exec1)
        QtCore.QMetaObject.connectSlotsByName(Sell)

    def retranslateUi(self, Sell):
        _translate = QtCore.QCoreApplication.translate
        Sell.setWindowTitle(_translate("Sell", "Dialog"))
        self.label.setText(_translate("Sell", "身份证号："))
        self.label_2.setText(_translate("Sell", "购买票数："))
        self.credit.setHtml(_translate("Sell", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'微软雅黑\';\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Sell", "应付钱数："))
        self.sum.setHtml(_translate("Sell", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">100.0</span></p></body></html>"))
        self.label_4.setText(_translate("Sell", "元"))
        self.print.setText(_translate("Sell", "打印机票"))
        self.execbtn.setText(_translate("Sell", "退出"))

