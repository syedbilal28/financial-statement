# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accounting_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 213)
        self.Next = QtWidgets.QPushButton(Dialog)
        self.Next.setGeometry(QtCore.QRect(294, 180, 81, 23))
        self.Next.setObjectName("Next")
        self.Submit = QtWidgets.QPushButton(Dialog)
        self.Submit.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.Submit.setObjectName("Submit")
        self.Credit = QtWidgets.QLineEdit(Dialog)
        self.Credit.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.Credit.setObjectName("Credit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label_6.setObjectName("label_6")
        self.Debit = QtWidgets.QLineEdit(Dialog)
        self.Debit.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.Debit.setObjectName("Debit")
        self.Value = QtWidgets.QLineEdit(Dialog)
        self.Value.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.Value.setObjectName("Value")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 47, 13))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Next.setText(_translate("Dialog", "Trial Balance"))
        self.Submit.setText(_translate("Dialog", "Submit"))
        self.label_5.setText(_translate("Dialog", "Credit:"))
        self.label_6.setText(_translate("Dialog", "Value:"))
        self.label_7.setText(_translate("Dialog", "Debit:"))
        self.pushButton.setText(_translate("Dialog", "Journal"))

# if __name__ == "__main__":
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())