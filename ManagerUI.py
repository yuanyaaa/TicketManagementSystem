from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(903, 596)
        Manager.setStyleSheet("#Manager{border-image: url(./bg_5.jpg);}")
        self.trainbtn = QtWidgets.QPushButton(Manager)
        self.trainbtn.setGeometry(QtCore.QRect(80, 200, 151, 61))
        self.trainbtn.setStyleSheet("QPushButton{\n"
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
        self.trainbtn.setObjectName("trainbtn")
        self.stationbtn = QtWidgets.QPushButton(Manager)
        self.stationbtn.setGeometry(QtCore.QRect(80, 290, 151, 61))
        self.stationbtn.setStyleSheet("QPushButton{\n"
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
        self.stationbtn.setObjectName("stationbtn")
        self.trainnumbtn = QtWidgets.QPushButton(Manager)
        self.trainnumbtn.setGeometry(QtCore.QRect(80, 380, 151, 61))
        self.trainnumbtn.setStyleSheet("QPushButton{\n"
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
        self.trainnumbtn.setObjectName("trainnumbtn")
        self.pushButton_4 = QtWidgets.QPushButton(Manager)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 200, 151, 61))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Manager)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 290, 151, 61))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Manager)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 200, 161, 61))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(Manager)
        self.line.setGeometry(QtCore.QRect(290, 130, 20, 461))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Manager)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 901, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Manager)
        self.line_3.setGeometry(QtCore.QRect(570, 130, 20, 461))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(Manager)
        self.label.setGeometry(QtCore.QRect(90, 80, 151, 31))
        self.label.setStyleSheet("font: 16pt \"楷体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Manager)
        self.label_2.setGeometry(QtCore.QRect(390, 80, 121, 31))
        self.label_2.setStyleSheet("font: 16pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Manager)
        self.label_3.setGeometry(QtCore.QRect(680, 80, 121, 31))
        self.label_3.setStyleSheet("font: 16pt \"楷体\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Manager)
        self.trainbtn.clicked.connect(Manager.updatetrain)
        self.stationbtn.clicked.connect(Manager.updatestation)
        self.trainnumbtn.clicked.connect(Manager.updatedeparturetime)
        self.pushButton_4.clicked.connect(Manager.addconductor)
        self.pushButton_5.clicked.connect(Manager.addmanager)
        self.pushButton_6.clicked.connect(Manager.showsell)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        _translate = QtCore.QCoreApplication.translate
        Manager.setWindowTitle(_translate("Manager", "管理员界面"))
        self.trainbtn.setText(_translate("Manager", "飞机修改"))
        self.stationbtn.setText(_translate("Manager", "机场修改"))
        self.trainnumbtn.setText(_translate("Manager", "航班修改"))
        self.pushButton_4.setText(_translate("Manager", "售票员管理"))
        self.pushButton_5.setText(_translate("Manager", "管理员管理"))
        self.pushButton_6.setText(_translate("Manager", "售票统计"))
        self.label.setText(_translate("Manager", "调度功能"))
        self.label_2.setText(_translate("Manager", "维护功能"))
        self.label_3.setText(_translate("Manager", "统计功能"))

