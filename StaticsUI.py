from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Statics(object):
    def setupUi(self, Statics):
        Statics.setObjectName("Statics")
        Statics.resize(818, 569)
        self.detail = QtWidgets.QTableWidget(Statics)
        self.detail.setGeometry(QtCore.QRect(400, 20, 381, 521))
        self.detail.setObjectName("detail")
        self.detail.setColumnCount(3)
        self.detail.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detail.setHorizontalHeaderItem(2, item)
        self.widget = QtWidgets.QWidget(Statics)
        self.widget.setGeometry(QtCore.QRect(0, 0, 361, 571))
        self.widget.setStyleSheet("border-image: url(./bg_SellUI.png);")
        self.widget.setObjectName("widget")

        self.retranslateUi(Statics)
        QtCore.QMetaObject.connectSlotsByName(Statics)

    def retranslateUi(self, Statics):
        _translate = QtCore.QCoreApplication.translate
        Statics.setWindowTitle(_translate("Statics", "Dialog"))
        item = self.detail.horizontalHeaderItem(0)
        item.setText(_translate("Statics", "员工号"))
        item = self.detail.horizontalHeaderItem(1)
        item.setText(_translate("Statics", "员工姓名"))
        item = self.detail.horizontalHeaderItem(2)
        item.setText(_translate("Statics", "共计卖出票数"))

