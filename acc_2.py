# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Accounting Cycle")
        Dialog.resize(643, 602)
        Dialog.setStyleSheet("background-color: rgb(205, 255, 255);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 541))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Debit = QtWidgets.QComboBox(self.tab)
        self.Debit.setGeometry(QtCore.QRect(90, 200, 151, 31))
        self.Debit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Debit.setEditable(True)
        self.Debit.setObjectName("Debit")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.Debit.addItem("")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 200, 47, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 270, 47, 21))
        self.label_2.setObjectName("label_2")
        self.Credit = QtWidgets.QComboBox(self.tab)
        self.Credit.setGeometry(QtCore.QRect(90, 260, 151, 31))
        self.Credit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(218, 218, 218);")
        self.Credit.setEditable(True)
        self.Credit.setObjectName("Credit")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Credit.addItem("")
        self.Submit = QtWidgets.QPushButton(self.tab)
        self.Submit.setGeometry(QtCore.QRect(510, 320, 101, 41))
        self.Submit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Submit.setObjectName("Submit")
        self.AnotherDebit = QtWidgets.QPushButton(self.tab)
        self.AnotherDebit.setGeometry(QtCore.QRect(510, 200, 101, 31))
        self.AnotherDebit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AnotherDebit.setObjectName("AnotherDebit")
        self.AnotherCredit = QtWidgets.QPushButton(self.tab)
        self.AnotherCredit.setGeometry(QtCore.QRect(510, 260, 101, 31))
        self.AnotherCredit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AnotherCredit.setObjectName("AnotherCredit")
        self.DebitValue = QtWidgets.QLineEdit(self.tab)
        self.DebitValue.setGeometry(QtCore.QRect(340, 200, 151, 31))
        self.DebitValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DebitValue.setObjectName("DebitValue")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(270, 200, 47, 21))
        self.label_4.setObjectName("label_4")
        self.CreditValue = QtWidgets.QLineEdit(self.tab)
        self.CreditValue.setGeometry(QtCore.QRect(340, 260, 151, 31))
        self.CreditValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CreditValue.setObjectName("CreditValue")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(270, 270, 47, 21))
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(469, 20, 131, 41))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(226, 226, 226);")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.PreviousEntry = QtWidgets.QLabel(self.tab)
        self.PreviousEntry.setGeometry(QtCore.QRect(90, 310, 401, 81))
        self.PreviousEntry.setText("")
        self.PreviousEntry.setObjectName("PreviousEntry")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 321, 61))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 621, 521))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(-5, -9, 621, 531))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(-10, -10, 631, 531))
        self.tableWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 621, 521))
        self.tableWidget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(10)
        self.tableWidget_4.setRowCount(0)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 621, 521))
        self.tableWidget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(7)
        self.tableWidget_5.setRowCount(0)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 621, 521))
        self.tableWidget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tabWidget.addTab(self.tab_7, "")
        self.ShowTrial = QtWidgets.QPushButton(Dialog)
        self.ShowTrial.setGeometry(QtCore.QRect(550, 560, 81, 41))
        self.ShowTrial.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ShowTrial.setObjectName("ShowTrial")
        self.ShowJournal = QtWidgets.QPushButton(Dialog)
        self.ShowJournal.setGeometry(QtCore.QRect(450, 560, 81, 41))
        self.ShowJournal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ShowJournal.setObjectName("ShowJournal")
        self.ShowLedger = QtWidgets.QPushButton(Dialog)
        self.ShowLedger.setGeometry(QtCore.QRect(350, 560, 81, 41))
        self.ShowLedger.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ShowLedger.setObjectName("ShowLedger")
        self.Income = QtWidgets.QPushButton(Dialog)
        self.Income.setGeometry(QtCore.QRect(230, 560, 111, 41))
        self.Income.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Income.setObjectName("Income")
        self.Balance = QtWidgets.QPushButton(Dialog)
        self.Balance.setGeometry(QtCore.QRect(130, 560, 91, 41))
        self.Balance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Balance.setObjectName("Balance")
        self.Close_pre = QtWidgets.QPushButton(Dialog)
        self.Close_pre.setGeometry(QtCore.QRect(20, 560, 101, 41))
        self.Close_pre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Close_pre.setObjectName("Close_pre")
        self.ShowTrial.raise_()
        self.ShowJournal.raise_()
        self.ShowLedger.raise_()
        self.Income.raise_()
        self.Balance.raise_()
        self.Close_pre.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Debit.setItemText(0, _translate("Dialog", None))
        self.Debit.setItemText(1, _translate("Dialog", "Cash"))
        self.Debit.setItemText(2, _translate("Dialog", "Accounts Receivable"))
        self.Debit.setItemText(3, _translate("Dialog", "Notes Receivable"))
        self.Debit.setItemText(4, _translate("Dialog", "Supplies"))
        self.Debit.setItemText(5, _translate("Dialog", "Equipment"))
        self.Debit.setItemText(6, _translate("Dialog", "Accounts Payable"))
        self.Debit.setItemText(7, _translate("Dialog", "Notes Payable"))
        self.Debit.setItemText(8, _translate("Dialog", "Unearned Revenue"))
        self.Debit.setItemText(9, _translate("Dialog", "Service Revenue"))
        self.Debit.setItemText(10, _translate("Dialog", "Capital"))
        self.Debit.setItemText(11, _translate("Dialog", "Drawings"))
        self.Debit.setItemText(12, _translate("Dialog", "Rent Expense"))
        self.Debit.setItemText(13, _translate("Dialog", "Salaries Expense"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Debit</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Credit</span></p></body></html>"))
        self.Credit.setItemText(0, _translate("Dialog", None))
        self.Credit.setItemText(1, _translate("Dialog", "Cash"))
        self.Credit.setItemText(2, _translate("Dialog", "Accounts Receivable"))
        self.Credit.setItemText(3, _translate("Dialog", "Notes Receivable"))
        self.Credit.setItemText(4, _translate("Dialog", "Supplies"))
        self.Credit.setItemText(5, _translate("Dialog", "Equipment"))
        self.Credit.setItemText(6, _translate("Dialog", "Accounts Payable"))
        self.Credit.setItemText(7, _translate("Dialog", "Notes Payable"))
        self.Credit.setItemText(8, _translate("Dialog", "Unearned Revenue"))
        self.Credit.setItemText(9, _translate("Dialog", "Service Revenue"))
        self.Credit.setItemText(10, _translate("Dialog", "Capital"))
        self.Credit.setItemText(11, _translate("Dialog", "Drawings"))
        self.Credit.setItemText(12, _translate("Dialog", "Rent Expense"))
        self.Credit.setItemText(13, _translate("Dialog", "Salaries Expense"))
        self.Submit.setText(_translate("Dialog", "Submit"))
        self.AnotherDebit.setText(_translate("Dialog", "Another Debit"))
        self.AnotherCredit.setText(_translate("Dialog", "Another Credit"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Value</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Value</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Usman Institute of Technology</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Journal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Trial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Balance Sheet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Income Statement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Closing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Page"))
        self.ShowTrial.setText(_translate("Dialog", "Trial"))
        self.ShowJournal.setText(_translate("Dialog", "Journal"))
        self.ShowLedger.setText(_translate("Dialog", "Ledger"))
        self.Income.setText(_translate("Dialog", "Income Statement"))
        self.Balance.setText(_translate("Dialog", "BalanceSheet"))
        self.Close_pre.setText(_translate("Dialog", "Closing"))