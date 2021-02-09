'''
* @Author: csy 
* @Date: 2019-05-09 15:13:52 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-09 15:13:52 
'''
import sys
from PyQt5 import QtWidgets

'''
    【简介】
	第一个PyQt例子
   
    
'''

app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication类，作为GUI主程序入口
widget = QtWidgets.QWidget()  # 实例化widget窗口
widget.resize(360, 360)  # 设置窗口大小
widget.setWindowTitle("Hello,PyQt5")  # 设置窗口标题
widget.show()  # 显示窗口
sys.exit(app.exec_())  # 进入该程序的主循环。调用exit()或主部件被销毁，主循环就会结束
