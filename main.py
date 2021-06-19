from Login import Login
from Conductor import Conductor
import Sell
import Refund
from Manager import Manager
import Dispatch
import Statics
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    conductorui = Conductor()
    managerui = Manager()
    loginui = Login(conductorui, managerui)
    loginui.show()
    sys.exit(app.exec())
