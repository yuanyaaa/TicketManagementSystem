import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ConductorUI import Ui_Dialog
from PyQt5.QtWidgets import QTableWidgetItem


class Conductor(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(Conductor, self).__init__()
        self.setupUi(self)

    def connectDB(self,conn, conductor):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.conductor = conductor

        self.cur.execute("select s_sname from station;")
        tmp = self.cur.fetchall()
        slist = []
        for item in tmp:
            slist.append(item[0])#因为返回的结果是[(a,), (b,)]型的
        self.aimstation.addItems(slist)


    def searchdetail(self):
        self.cur.execute("select * from searchdetail( '"+self.aimstation.currentText()
                         +"', cast("+str(self.month.value())+ " as smallint), cast("+ str(self.date.value()) + " as smallint));")
        tmp = self.cur.fetchall()
        tmp = set(tmp)
        self.detail.setRowCount(len(tmp))
        for i, item in enumerate(tmp):
            for j, jtem in enumerate(item):
                if jtem == None:
                    break
                newitem = QTableWidgetItem(jtem)
                self.detail.setItem(i, j, newitem)
        self.detail.verticalHeader().sectionClicked.connect(self.versectionclicked)
        # self.cur.close()
        # self.conn.close()

    def versectionclicked(self, index):
        #车次
        trainnum = self.detail.selectedItems()[0].text()
        self.cur.execute("select dt_cost from departuretime where dt_trainnum = '"+trainnum+"'")
        self.pricenum = self.cur.fetchall()[0][0]
        self.price.setText(str(self.pricenum))
        #剩票
        self.cur.execute("select * from calcRestTicket('"+trainnum+"');")
        self.restnum = self.cur.fetchall()[0][0]
        self.rest.setText(str(self.restnum))

    def tosell(self):
        # 车次
        trainnum = self.detail.selectedItems()[0].text()
        self.sellui = Sell()
        self.sellui.connectDB(self.conn, trainnum, self.month.value(), self.date.value(),
                              self.aimstation.currentText(), self.pricenum, self.restnum, self.conductor)
        self.sellui.show()

    def torefund(self):
        self.refundui = Refund()
        self.refundui.connectDB(self.conn)
        self.refundui.show()

    def exit(self):
        self.cur.close()
        self.conn.close()
        self.close()