'''
* @Author: csy 
* @Date: 2019-05-09 15:23:59 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-09 15:23:59 
'''
# -*- coding: utf-8 -*-
'''
    【简介】
	PyQT5的第一个简单例子
   
  
'''


import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.move(300, 300)  # 移动到（300,300）
window.setWindowTitle('hello PyQt5')
window.show()
sys.exit(app.exec_())
