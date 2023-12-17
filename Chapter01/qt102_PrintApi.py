'''
* @Author: csy 
* @Date: 2019-05-09 15:16:45 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-09 15:16:45 
'''
# -*- coding: utf-8 -*-
'''
    【简介】
	保存PyQt5类的使用手册到本地
   
    
'''


import sys
from PyQt5.QtWidgets import QWidget
out = sys.stdout
sys.stdout = open(r'D:\\Desktop\\1.txt', 'w')  # 打开桌面1.txt文档
print("打印QWidget方法和属性：\n", dir(QWidget))
print("\n\n\n打印QWidget帮助信息：\n")
help(QWidget)
sys.stdout.close()
sys.stdout = out
