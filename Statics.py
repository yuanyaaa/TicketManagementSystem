import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QTableWidgetItem
from StaticsUI import Ui_Statics

class Statics(QtWidgets.QDialog, Ui_Statics):
    def __init__(self, conn):
        super(Statics, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.cur = conn.cursor()
        self.cur.execute("select * from c_tc order by count desc;")
        tmp = self.cur.fetchall()
        tmp = set(tmp)
        self.detail.setRowCount(len(tmp))
        for i, item in enumerate(tmp):
            for j, jtem in enumerate(item):
                if jtem == None:
                    break;
                newitem = QTableWidgetItem(str(jtem))
                newitem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.detail.setItem(i, j, newitem)