import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from LoginUI import Ui_Form
from PyQt5.QtWidgets import  QTableWidgetItem

class Login(QtWidgets.QWidget, Ui_Form):
    #初始化
    def __init__(self, conductorui, managerui):
        super(Login, self).__init__()
        self.setupUi(self)
        self.conductorui = conductorui
        self.managerui = managerui

    #登录
    def accept(self):
        #管理员选择
        if(self.ifmanager.isChecked()):
            #连接数据库
            self.conn = pymysql.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="3306")
            #conn传递
            self.managerui.connectDB(self.conn)
            #管理员窗口显示并关闭登录界面
            self.managerui.show()
            self.close()
            
        #售票员选择
        elif(self.ifconductor.isChecked()):
            #连接数据库
            self.conn = pymysql.connect(database="TicketManagementSystem", user=self.nametext.toPlainText(),
                                         password=self.passwordtext.toPlainText(), host="localhost", port="5432")
            #conn传递
            self.conductorui.connectDB(self.conn, self.nametext.toPlainText())
            #售票员窗口显示并关闭登录界面
            self.conductorui.show()
            self.close()
        else:
            #弹出窗口，说不能不选择角色就登录
            #未实现
            pass

    #退出
    def exec(self):
        sys.exit(app.exec())