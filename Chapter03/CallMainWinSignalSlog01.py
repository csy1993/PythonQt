'''
* @Author: csy 
* @Date: 2019-05-16 10:08:45 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-16 10:08:45 
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlog01 import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
