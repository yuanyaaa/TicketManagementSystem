from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 507)
        Form.setStyleSheet("#Form{border-image: url(./bg_LoginUI.jpg);}")
        self.ifmanager = QtWidgets.QRadioButton(Form)
        self.ifmanager.setGeometry(QtCore.QRect(190, 130, 131, 31))
        self.ifmanager.setStyleSheet("font: 14pt \"楷体\";\n"
                                     "color: rgb(0, 255, 255);")
        self.ifmanager.setObjectName("ifmanager")
        self.ifconductor = QtWidgets.QRadioButton(Form)
        self.ifconductor.setGeometry(QtCore.QRect(470, 130, 131, 31))
        self.ifconductor.setStyleSheet("font: 14pt \"楷体\";\n"
                                       "color: rgb(0, 255, 255);")
        self.ifconductor.setObjectName("ifconductor")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 50, 351, 61))
        self.label.setStyleSheet("font: 20pt \"楷体\";\n"
                                 "color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.nametext = QtWidgets.QTextEdit(Form)
        self.nametext.setGeometry(QtCore.QRect(310, 210, 291, 31))
        self.nametext.setObjectName("nametext")
        self.passwordtext = QtWidgets.QTextEdit(Form)
        self.passwordtext.setGeometry(QtCore.QRect(310, 280, 291, 31))
        self.passwordtext.setObjectName("passwordtext")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 210, 91, 31))
        self.label_2.setStyleSheet("font: 15pt \"楷体\";\n"
                                   "color: rgb(0, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 280, 91, 31))
        self.label_3.setStyleSheet("font: 15pt \"楷体\";\n"
                                   "color: rgb(0, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setGeometry(QtCore.QRect(180, 360, 171, 51))
        self.ok.setStyleSheet("QPushButton{\n"
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
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(440, 360, 171, 51))
        self.cancel.setStyleSheet("QPushButton{\n"
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
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Form)
        # self.ok.clicked.connect(Form.accept)
        # self.cancel.clicked.connect(Form.exec())
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文渊机票售票系统V1.0"))
        self.ifmanager.setText(_translate("Form", "管理员"))
        self.ifconductor.setText(_translate("Form", "售票员"))
        self.label.setText(_translate("Form", "文渊机票售票系统"))
        self.label_2.setText(_translate("Form", "用户名："))
        self.label_3.setText(_translate("Form", "密  码："))
        self.ok.setText(_translate("Form", "确定"))
        self.cancel.setText(_translate("Form", "退出"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
