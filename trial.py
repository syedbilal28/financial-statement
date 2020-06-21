# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trial.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import sqlalchemy
import os
import sys
class Ui_Dialog(object):
    def loadData(self):


        conn = sqlalchemy.engine.create_engine("sqlite:///"+ os.path.abspath("./data1.db"))

        result = conn.execute("Select * from Accounts")
        row_position = self.Database.RowCount()
        for row_count, row_data in enumerate(result):
            self.Database.insertrow(row_count)
            for column_count,data in enumerate(row_data):
                self.Database.setItem(row_count,column_count,QtWidgets.QTableWidgetItem(str(data)))
        conn.dispose()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 436)
        self.Database = QtWidgets.QTableView(Dialog)
        self.Database.setGeometry(QtCore.QRect(10, 10, 371, 411))
        self.Database.setObjectName("Database")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    def rowCount(self, parent=None):
        return self.data.shape[0]

    def columnCount(self, parent=None):
        return self.data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.data.columns[col]
        return None

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    w = Ui_Dialog()
    w.setupUi(MainWindow)
    w.loadData()
    w.show()
    sys.exit(app.exec_())