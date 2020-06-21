# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ledger.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import AccountingCycle
class Ui_Ledger(object):
    # def __init__(self):
    #
    #     self.LedgerOK.clicked.connect(self.Ledgertable())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Ledger")
        Dialog.resize(400, 300)
        self.LedgerTable = QtWidgets.QTableWidget(Dialog)
        self.LedgerTable.setGeometry(QtCore.QRect(20, 70, 256, 192))
        self.LedgerTable.setObjectName("LedgerTable")
        self.LedgerTable.setColumnCount(2)
        self.LedgerTable.setRowCount(1)
        self.LedgerCombo = QtWidgets.QComboBox(Dialog)
        self.LedgerCombo.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.LedgerCombo.setObjectName("LedgerCombo")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerCombo.addItem("")
        self.LedgerOK = QtWidgets.QPushButton(Dialog)
        self.LedgerOK.setGeometry(QtCore.QRect(290, 20, 101, 41))
        self.LedgerOK.setObjectName("LedgerOK")
        #self.LedgerOK.clicked.connect(self.Ledgertable())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.LedgerCombo.setItemText(0, _translate("Dialog", "Cash"))
        self.LedgerCombo.setItemText(1, _translate("Dialog", "Accounts Receivable"))
        self.LedgerCombo.setItemText(2, _translate("Dialog", "Notes Receivable"))
        self.LedgerCombo.setItemText(3, _translate("Dialog", "Supplies"))
        self.LedgerCombo.setItemText(4, _translate("Dialog", "Equipment"))
        self.LedgerCombo.setItemText(5, _translate("Dialog", "Accumulated - Depreciation Equipment"))
        self.LedgerCombo.setItemText(6, _translate("Dialog", "Accounts Payable"))
        self.LedgerCombo.setItemText(7, _translate("Dialog", "Notes Payable"))
        self.LedgerCombo.setItemText(8, _translate("Dialog", "Unearned Revenue"))
        self.LedgerCombo.setItemText(9, _translate("Dialog", "Capital"))
        self.LedgerCombo.setItemText(10, _translate("Dialog", "Drawings"))
        self.LedgerCombo.setItemText(11, _translate("Dialog", "Service Revenue"))
        self.LedgerCombo.setItemText(12, _translate("Dialog", "Advertising Expense"))
        self.LedgerCombo.setItemText(13, _translate("Dialog", "Prepaid Insurance"))
        self.LedgerCombo.setItemText(14, _translate("Dialog", "Interest Payable"))
        self.LedgerCombo.setItemText(15, _translate("Dialog", "Interest Expense"))
        self.LedgerCombo.setItemText(16, _translate("Dialog", "Supplies Expense"))
        self.LedgerCombo.setItemText(17, _translate("Dialog", "Gasoline Expense"))
        self.LedgerCombo.setItemText(18, _translate("Dialog", "Salaries Payable"))
        self.LedgerCombo.setItemText(19, _translate("Dialog", "Maintenance and Repairs Expense"))
        self.LedgerCombo.setItemText(20, _translate("Dialog", "Depreciation Expense"))
        self.LedgerCombo.setItemText(21, _translate("Dialog", "Insurance Expense"))
        self.LedgerCombo.setItemText(22, _translate("Dialog", "Salaries Expense"))
        self.LedgerCombo.setItemText(23, _translate("Dialog", "Utilities Expense"))
        self.LedgerCombo.setItemText(24, _translate("Dialog", "Rent Expense"))
        self.LedgerOK.setText(_translate("Dialog", "OK"))
    def Ledgertable(self):
        Account= str(self.LedgerCombo.currentText())
        led = AccountingCycle.AccountingCycle()
        number = led.accountnumbers[Account]

        conn = led.engine.connect()
        rows = conn.execute("Select * from '{}'".format(number))
        rows= rows.fetchall()
        self.LedgerTable.setRowCount(0)
        self.LedgerTable.setRowCount(1)
        self.LedgerTable.setItem(0, 0, QtWidgets.QTableWidgetItem("Debit"))
        self.LedgerTable.setItem(0, 1, QtWidgets.QTableWidgetItem("Credit"))
        for i in range(len(rows)):

            self.LedgerTable.insertRow(i+1)

            for j in range(2):
                self.LedgerTable.setItem(i+1,j,QtWidgets.QTableWidgetItem(str(rows[i][j])))
