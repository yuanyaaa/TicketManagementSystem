from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(951, 662)
        Dialog.setStyleSheet("#Dialog{border-image: url(./bg8.jpg);}\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(740, 90, 101, 31))
        self.label.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.aimstation = QtWidgets.QComboBox(Dialog)
        self.aimstation.setGeometry(QtCore.QRect(740, 130, 161, 31))
        self.aimstation.setStyleSheet("font: 14pt \"Academy Engraved LET\";")
        self.aimstation.setObjectName("aimstation")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(740, 190, 101, 31))
        self.label_2.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 390, 121, 31))
        self.label_3.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.detail = QtWidgets.QTableWidget(Dialog)
        self.detail.setGeometry(QtCore.QRect(70, 50, 631, 301))
        self.detail.setStyleSheet("font: 14pt \"楷体\";")
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 390, 121, 31))
        self.label_5.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(50, 530, 181, 71))
        self.find.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.find.setObjectName("find")
        self.sell = QtWidgets.QPushButton(Dialog)
        self.sell.setGeometry(QtCore.QRect(250, 530, 181, 71))
        self.sell.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.sell.setObjectName("sell")
        self.refund = QtWidgets.QPushButton(Dialog)
        self.refund.setGeometry(QtCore.QRect(450, 530, 191, 71))
        self.refund.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.refund.setObjectName("refund")
        self.month = QtWidgets.QSpinBox(Dialog)
        self.month.setGeometry(QtCore.QRect(790, 190, 61, 31))
        self.month.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.date = QtWidgets.QSpinBox(Dialog)
        self.date.setGeometry(QtCore.QRect(790, 250, 61, 31))
        self.date.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.date.setMinimum(1)
        self.date.setMaximum(31)
        self.date.setObjectName("date")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(740, 250, 101, 31))
        self.label_7.setStyleSheet("font: 15pt \"楷体\";\n"
"color: rgb(255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.price = QtWidgets.QTextEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(200, 390, 161, 41))
        self.price.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.price.setObjectName("price")
        self.rest = QtWidgets.QTextEdit(Dialog)
        self.rest.setGeometry(QtCore.QRect(650, 390, 161, 41))
        self.rest.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.rest.setObjectName("rest")
        self.exitbtn = QtWidgets.QPushButton(Dialog)
        self.exitbtn.setGeometry(QtCore.QRect(670, 530, 191, 71))
        self.exitbtn.setStyleSheet("QPushButton{\n"
"border-style:outset;\n"
"font: 14pt \"楷体\";\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 14pt \"楷体\";\n"
"}")
        self.exitbtn.setObjectName("exitbtn")

        self.retranslateUi(Dialog)
        self.find.clicked.connect(Dialog.searchdetail)
        self.sell.clicked.connect(Dialog.tosell)
        self.refund.clicked.connect(Dialog.torefund)
        self.exitbtn.clicked.connect(Dialog.exit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "售票员界面"))
        self.label.setText(_translate("Dialog", "目标站："))
        self.label_2.setText(_translate("Dialog", "月："))
        self.label_3.setText(_translate("Dialog", "票    价："))
        item = self.detail.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "航班"))
        item = self.detail.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "终点站"))
        item = self.detail.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "机型"))
        item = self.detail.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "起飞时间"))
        item = self.detail.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "登机口"))
        self.label_5.setText(_translate("Dialog", "剩余机票："))
        self.find.setText(_translate("Dialog", "查找"))
        self.sell.setText(_translate("Dialog", "销售"))
        self.refund.setText(_translate("Dialog", "退票"))
        self.label_7.setText(_translate("Dialog", "日："))
        self.rest.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.exitbtn.setText(_translate("Dialog", "退出"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

