import pymysql
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from Dispatch import Dispatch
from ManagerUI import Ui_Manager


class Manager(QtWidgets.QDialog, Ui_Manager):
    def __init__(self):
        super(Manager, self).__init__()
        self.setupUi(self)

    def connectDB(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def updatetrain(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 0)
        self.dispatchui.show()

    def updatestation(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 1)
        self.dispatchui.show()

    def updatedeparturetime(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 2)
        self.dispatchui.show()

    def addconductor(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 3)
        self.dispatchui.show()

    def addmanager(self):
        self.dispatchui = Dispatch()
        self.dispatchui.connectDB(self.conn, 4)
        self.dispatchui.show()

    def showsell(self):
        self.staticsui = Statics(self.conn)
        self.staticsui.show()
