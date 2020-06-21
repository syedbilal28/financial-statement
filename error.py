# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Error")
        Dialog.resize(400, 120)
        # self.OK = QtWidgets.QPushButton(Dialog)
        # self.OK.setGeometry(QtCore.QRect(150, 160, 91, 41))
        # self.OK.setObjectName("OK")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 281, 41))
        self.label.setObjectName("label")
        #self.OK.clicked.connect(self.close)
        #self.label.setGeometry(QtCore.QRect())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.OK.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Unbalanced equation</span></p></body></html>"))

