'''
* @Author: csy 
* @Date: 2019-05-09 17:17:35 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-09 17:17:35 
'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
from test4 import *
from test5 import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.child=ChildrenForm()
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childShow)
    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,"打开","c:/","All Files(*);;Text Files(*.txt)")
        self.statusbar.showMessage(file)
    def childShow(self):
        self.gridLayout.addWidget(self.child)
        self.child.show()


class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
