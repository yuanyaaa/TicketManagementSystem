import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QTableWidgetItem
from RefundUI import Ui_Refund

class Refund(QtWidgets.QDialog, Ui_Refund):
    def __init__(self):
        super(Refund, self).__init__()
        self.setupUi(self)

    def connectDB(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def searchcredit(self):
        self.cur.execute("select * from searchcredit('"+self.credit.toPlainText()+"');")
        tmp = self.cur.fetchall()
        self.detail.setRowCount(len(tmp))
        self.tcidlist = []
        for i, item in enumerate(tmp):
            sumi = len(item)
            for j, jtem in enumerate(item):
                if(j == sumi - 1):
                    self.tcidlist.append(jtem)
                    continue;
                newitem = QTableWidgetItem(str(jtem))
                self.detail.setItem(i, j, newitem)
        self.detail.clicked.connect(self.showrefundmoney)

    def showrefundmoney(self):
        row = self.detail.selectedItems()[0].row()
        tmp = float(self.detail.item(row, 3).text())
        self.backmoney.setText(str(tmp * 0.8))

    def exit(self):
        self.close()

    def comfirm(self):
        selectrow = self.detail.selectedItems()[0].row()
        self.cur.execute("select refundticket('"+self.tcidlist[selectrow]+"', "+str(self.backmoney.toPlainText())+");")
        self.cur.fetchall()
        self.conn.commit()
        self.close()