from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class Ui_Dispatch(object):
    def setupUi(self, Dispatch):
        Dispatch.setObjectName("Dispatch")
        Dispatch.resize(784, 530)
        Dispatch.setStyleSheet("#Dispatch{border-image: url(./bg1.jpg);}")
        self.detail = QtWidgets.QTableWidget(Dispatch)
        self.detail.setGeometry(QtCore.QRect(40, 120, 571, 301))
        self.detail.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(0)
        self.detail.setRowCount(0)
        self.title = QtWidgets.QLabel(Dispatch)
        self.title.setGeometry(QtCore.QRect(290, 60, 271, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 20pt \"楷体\";\n"
"color: rgb(0, 255, 255);")
        self.title.setObjectName("title")
        self.acceptbtn = QtWidgets.QPushButton(Dispatch)
        self.acceptbtn.setGeometry(QtCore.QRect(630, 190, 141, 61))
        self.acceptbtn.setStyleSheet("QPushButton{\n"
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
        self.acceptbtn.setObjectName("acceptbtn")
        self.cancelbtn = QtWidgets.QPushButton(Dispatch)
        self.cancelbtn.setGeometry(QtCore.QRect(630, 310, 141, 61))
        self.cancelbtn.setStyleSheet("QPushButton{\n"
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
        self.cancelbtn.setObjectName("cancelbtn")
        self.addbtn = QtWidgets.QPushButton(Dispatch)
        self.addbtn.setGeometry(QtCore.QRect(60, 440, 191, 51))
        self.addbtn.setStyleSheet("QPushButton{\n"
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
        self.addbtn.setObjectName("addbtn")
        self.deletebtn = QtWidgets.QPushButton(Dispatch)
        self.deletebtn.setGeometry(QtCore.QRect(330, 440, 221, 51))
        self.deletebtn.setStyleSheet("QPushButton{\n"
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
        self.deletebtn.setObjectName("deletebtn")

        self.retranslateUi(Dispatch)
        self.acceptbtn.clicked.connect(Dispatch.accept)
        self.cancelbtn.clicked.connect(Dispatch.exit)
        self.addbtn.clicked.connect(Dispatch.tableadd)
        self.deletebtn.clicked.connect(Dispatch.tabledelete)
        QtCore.QMetaObject.connectSlotsByName(Dispatch)

    def retranslateUi(self, Dispatch):
        _translate = QtCore.QCoreApplication.translate
        Dispatch.setWindowTitle(_translate("Dispatch", "信息修改"))
        self.title.setText(_translate("Dispatch", "飞机信息修改"))
        self.acceptbtn.setText(_translate("Dispatch", "确定"))
        self.cancelbtn.setText(_translate("Dispatch", "取消"))
        self.addbtn.setText(_translate("Dispatch", "增加"))
        self.deletebtn.setText(_translate("Dispatch", "删除"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QDialog()
    ui = Ui_Dispatch()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())