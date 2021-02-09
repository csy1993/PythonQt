# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(False)
        Form.resize(912, 765)
        self.CloseWindows = QtWidgets.QPushButton(Form)
        self.CloseWindows.setGeometry(QtCore.QRect(360, 320, 75, 23))
        self.CloseWindows.setObjectName("CloseWindows")

        self.retranslateUi(Form)
        self.CloseWindows.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseWindows.setText(_translate("Form", "关闭窗口"))

