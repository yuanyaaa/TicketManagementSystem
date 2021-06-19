from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Refund(object):
    def setupUi(self, Refund):
        Refund.setObjectName("Refund")
        Refund.resize(934, 582)
        Refund.setStyleSheet("#Refund{border-image: url(./bg10.png);}\n"
"")
        self.label = QtWidgets.QLabel(Refund)
        self.label.setGeometry(QtCore.QRect(170, 370, 121, 31))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.detail = QtWidgets.QTableWidget(Refund)
        self.detail.setGeometry(QtCore.QRect(170, 40, 641, 311))
        self.detail.setStyleSheet("font: 12pt \"楷体\";")
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(5)
        self.detail.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(4, item)
        self.credit = QtWidgets.QTextEdit(Refund)
        self.credit.setGeometry(QtCore.QRect(170, 410, 271, 41))
        self.credit.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.credit.setObjectName("credit")
        self.search = QtWidgets.QPushButton(Refund)
        self.search.setGeometry(QtCore.QRect(170, 480, 161, 51))
        self.search.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.search.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.search.setObjectName("search")
        self.refundbtn = QtWidgets.QPushButton(Refund)
        self.refundbtn.setGeometry(QtCore.QRect(420, 480, 161, 51))
        self.refundbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.refundbtn.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.refundbtn.setObjectName("refundbtn")
        self.exitbtn = QtWidgets.QPushButton(Refund)
        self.exitbtn.setGeometry(QtCore.QRect(660, 480, 171, 51))
        self.exitbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.exitbtn.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.exitbtn.setObjectName("exitbtn")
        self.label_2 = QtWidgets.QLabel(Refund)
        self.label_2.setGeometry(QtCore.QRect(590, 370, 121, 31))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.backmoney = QtWidgets.QTextEdit(Refund)
        self.backmoney.setGeometry(QtCore.QRect(590, 410, 141, 41))
        self.backmoney.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.backmoney.setObjectName("backmoney")
        self.label_3 = QtWidgets.QLabel(Refund)
        self.label_3.setGeometry(QtCore.QRect(740, 410, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"方正颜宋简体\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Refund)
        self.search.clicked.connect(Refund.searchcredit)
        self.refundbtn.clicked.connect(Refund.comfirm)
        self.exitbtn.clicked.connect(Refund.exit)
        QtCore.QMetaObject.connectSlotsByName(Refund)

    def retranslateUi(self, Refund):
        _translate = QtCore.QCoreApplication.translate
        Refund.setWindowTitle(_translate("Refund", "退票界面"))
        self.label.setText(_translate("Refund", "身份证号："))
        item = self.detail.horizontalHeaderItem(0)
        item.setText(_translate("Refund", "出发日期"))
        item = self.detail.horizontalHeaderItem(1)
        item.setText(_translate("Refund", "航班号"))
        item = self.detail.horizontalHeaderItem(2)
        item.setText(_translate("Refund", "目的地"))
        item = self.detail.horizontalHeaderItem(3)
        item.setText(_translate("Refund", "票价"))
        item = self.detail.horizontalHeaderItem(4)
        item.setText(_translate("Refund", "座位号"))
        self.credit.setHtml(_translate("Refund", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.search.setText(_translate("Refund", "查询"))
        self.refundbtn.setText(_translate("Refund", "退订"))
        self.exitbtn.setText(_translate("Refund", "退出"))
        self.label_2.setText(_translate("Refund", "返还钱数："))
        self.backmoney.setHtml(_translate("Refund", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Refund", "元"))

