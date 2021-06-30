import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import  QTableWidgetItem
from DispatchUI import Ui_Dispatch

class Dispatch(QtWidgets.QDialog, Ui_Dispatch):
    def __init__(self):
        super(Dispatch, self).__init__()
        self.setupUi(self)

    def connectDB(self, conn, type):
        self.conn = conn
        self.cur = conn.cursor()
        self.type = type
        if(type == 0):
            hlist = ['飞机ID', '飞机型', '座位数']
            self.attrs = ['t_tid', 't_ttype', 't_seatnum']
            self.cur.execute("select * from train;")
            list = self.cur.fetchall()
            self.title.setText('飞机修改')
            self.tablename = "train"
            self.pk = 't_tid'

        elif(type == 1):
            hlist = ['机场ID', '机场名', '机场经度', '机场纬度']
            self.attrs = ['s_sid', 's_sname', 's_slongitude', 's_slatitude']
            self.cur.execute("select * from station;")
            list = self.cur.fetchall()
            self.title.setText('机场修改')
            self.tablename = 'station'
            self.pk = 's_sid'

        elif(type == 2):
            hlist = ['航班','飞机ID', '目的地',  '起飞时间', '登机口', '出发月份', '出发日期', '机票价格']
            self.attrs = ['dt_trainnum', 'dt_tid', 'dt_aimsid',  'dt_departuretime', 'dt_ticketentrance', 'dt_month', 'dt_date', 'dt_cost']
            # self.attrs = ['dt_trainnum', 'dt_tid', 'dt_aimsid',  'dt_departuretime', 'dt_ticketentrance', 'dt_month', 'dt_date']
            self.cur.execute("select dt_trainnum,dt_tid, s_sname, dt_departuretime,   dt_ticketentrance, dt_month, dt_date, dt_cost from departuretime,station where dt_aimsid = s_sid;")
            # self.cur.execute("select dt_trainnum,dt_tid, s_sname, dt_departuretime,   dt_ticketentrance, dt_month, dt_date from departuretime,station where dt_aimsid = s_sid;")
            list = self.cur.fetchall()
            print(list)
            self.title.setText('航班修改')
            self.tablename = 'departuretime'
            self.pk = 'dt_trainnum'

        elif(type == 3):
            hlist = ['工号', '用户名', '密码']
            self.attrs = ['c_cid', 'c_cname', 'c_cpassword']
            self.cur.execute("select * from conductor;")
            list = self.cur.fetchall()
            self.title.setText('售票员管理')
            self.tablename = 'conductor'
            self.pk = 'c_cid'

        elif(type == 4):
            hlist = ['工号', '用户名', '密码']
            self.attrs = ['m_mid', 'm_mname', 'm_mpassword']
            self.cur.execute("select * from manager;")
            list = self.cur.fetchall()
            self.title.setText('管理员管理')
            self.tablename = 'manager'
            self.pk = 'm_mid'
            
        self.setdetail(hlist, list)

    def setdetail(self, hlist, list):
        # self.cur.execute("begin transaction;")
        self.detail.setColumnCount(len(hlist))
        self.detail.setHorizontalHeaderLabels(hlist)
        self.detail.setRowCount(len(list))
        self.tablelist = []
        for i, item in enumerate(list):
            line = []
            for j, jtem in enumerate(item):
                if jtem == None:
                    break
                line.append(str(jtem))
                newitem = QTableWidgetItem(str(jtem))
                if ((j == 0) and (self.type != 2)):
                    newitem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.detail.setItem(i, j, newitem)
            self.tablelist.append(line)

    def tableupdate(self):
        selects = self.detail.selectedItems()
        if(len(selects) == 0):
            return
        for s in selects:
            row = s.row()
            c = s.column()
            after = s.text()
            if c == 0:
                before = self.tablelist[row][0]
                self.tablelist[row][0] = after
            else:
                before = self.detail.item(row,0).text()
            if (self.type == 2 and c == 2):
                self.cur.execute("select s_sid from station where s_sname = '"+after+"';")
                after = self.cur.fetchall()[0][0]
            attr = self.attrs[c]
            print("update "+self.tablename+" set "+attr+" = '"
                          + after +"' where "+self.pk+" = '"+str(before)+"';")
            self.cur.execute("update "+self.tablename+" set "+attr+" = '"
                          + after +"' where "+self.pk+" = '"+str(before)+"';")
            if (self.type == 3 or self.type == 4) and (c == 2):
                print("alter user '" + self.tablelist[row][1] + "'@'localhost' identified by '" + str(after) + "';")
                self.cur.execute("alter user '"+ self.tablelist[row][1] +"'@'localhost' identified by '"+str(after)+"';")

    def tableadd(self):
        if(self.type == 1):
            self.cur.execute("select max(s_sid) from station;")
            res = self.cur.fetchall()[0][0]
            if res is None :
                res = 10011700
            tmp = [int(res)+1,'undefine', '0', '0']
            self.cur.execute("insert into station values({}, 'undefine', 0, 0);".format(tmp[0]))
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
        elif self.type == 0:
            self.cur.execute("select max(t_tid) from train;")
            res = self.cur.fetchall()[0][0]
            if res is None :
                res = 201912090
            tmp = [int(res) + 1, '超大飞机', 100]
            self.cur.execute("insert into train values ({}, \'{}\', {} );".format(tmp[0],tmp[1], tmp[2]))
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
        elif(self.type == 2):
            self.cur.execute("INSERT INTO departuretime(dt_tid, dt_aimsid, dt_trainnum, dt_departuretime, dt_ticketentrance, dt_month, dt_date, dt_cost) VALUES (201912091, 10011701, 0, '21-6-26 00:00:00', 0, 0, 0, 0);")
            # self.cur.execute("INSERT INTO departuretime(dt_tid, dt_aimsid, dt_trainnum, dt_departuretime, dt_ticketentrance, dt_month, dt_date) VALUES (201912091, 10011701, 0, '00:00:00', 0, 0, 0);")
            tmp = [0, '201912091', '10011701', '21-6-26 00:00:00', 0, 0, 0]
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
        elif(self.type == 3):
            self.cur.execute("select max(c_cid) from conductor;")
            i = self.cur.fetchall()[0][0]
            if i is None:
                i=1
            tmp = [int(i) + 1,'conductor0'+str(int(i) + 1) , '0']
            print("insert into conductor(c_cname, c_cpassword) values ('"+str(tmp[1])+"' , '0');")
            self.cur.execute("insert into conductor(c_cname, c_cpassword) values ('"+str(tmp[1])+"' , '0');")
            CreateCMD="create user '" + tmp[1] + "'@'localhost' identified by '" + tmp[2] + "';"
            self.cur.execute(CreateCMD)
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
            newitem = QTableWidgetItem(str(tmp[1]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 1, newitem)
        elif (self.type == 4):
            self.cur.execute("select max(m_mid) from manager;")
            i = self.cur.fetchall()[0][0]
            if i is None:
                i=1
            tmp = [int(i) + 1, 'manager0' + str(int(i)+1), '0']
            InsertCMD="insert into manager(m_mid,m_mname, m_mpassword) values ('" +str(tmp[0])+"' ,'"+ str(tmp[1]) + "' , '0');"
            print(InsertCMD)
            self.cur.execute(InsertCMD)
            CreateCMD="create user '" + tmp[1] + "'@'localhost' identified by '" + tmp[2] + "';"
            self.cur.execute(CreateCMD)
            self.tablelist.append(tmp)
            cnt = self.detail.rowCount()
            self.detail.setRowCount(cnt + 1)
            newitem = QTableWidgetItem(str(tmp[0]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 0, newitem)
            newitem = QTableWidgetItem(str(tmp[1]))
            newitem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.detail.setItem(cnt, 1, newitem)

    def tabledelete(self):
        row = self.detail.selectedItems()[0].row()
        item = self.detail.item(row, 0).text()
        print(item)
        print("delete from "+self.tablename+" where "+self.pk+" = '"+str(item)+"';")
        self.cur.execute("delete from " + self.tablename + " where " + self.pk + " = '" + str(item) + "';")
        if (self.type == 3 or self.type == 4):
            self.cur.execute("drop user '" + self.detail.item(row, 1).text() + "'@'localhost';")
        self.detail.removeRow(row)
        self.tablelist.remove(self.tablelist[row])


    def accept(self):
        self.conn.commit()
        self.close()

    def exit(self):
        self.conn.rollback()
        self.close()

