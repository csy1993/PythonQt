# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5中气泡提示
   
'''
  
import sys
from PyQt5.QtWidgets import QWidget, QToolTip , QApplication
from PyQt5.QtGui import QFont

class Winform(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(200, 300, 400, 400)
		self.setWindowTitle('气泡提示demo')
		QToolTip.setFont(QFont('SansSerif', 20))
		self.setToolTip('这是一个<b>气泡提示</b>')
		           
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec_())
