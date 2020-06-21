# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("New Account")
        Dialog.resize(699, 250)
        Dialog.setStyleSheet("background-color: rgb(211, 255, 253);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 601, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 140, 101, 31))
        self.label_3.setObjectName("label_3")
        self.nameinput = QtWidgets.QLineEdit(Dialog)
        self.nameinput.setGeometry(QtCore.QRect(130, 140, 181, 31))
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameinput.setObjectName("nameinput")
        self.numberinput = QtWidgets.QLineEdit(Dialog)
        self.numberinput.setGeometry(QtCore.QRect(450, 140, 161, 31))
        self.numberinput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numberinput.setObjectName("numberinput")
        self.AccountInput = QtWidgets.QPushButton(Dialog)
        self.AccountInput.setGeometry(QtCore.QRect(550, 200, 131, 41))
        self.AccountInput.setStyleSheet("\n"
"background-color: rgb(174, 221, 221);")
        self.AccountInput.setObjectName("AccountInput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">We are sorry for the inconveniece.Our data does not have the given accounts in database. </span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Please enter the account name and it\'s account number below.</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Account Name</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Account Number</span></p></body></html>"))
        self.AccountInput.setText(_translate("Dialog", "Enter Account"))
