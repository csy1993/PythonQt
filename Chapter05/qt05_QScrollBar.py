'''
* @Author: csy 
* @Date: 2019-05-22 15:01:57 
* @Last Modified by:   csy 
* @Last Modified time: 2019-05-22 15:01:57 
'''
# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QScrollBar 例子
   
  
'''




import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # hbox = QHBoxLayout( )
        # self.l1 = QLabel("拖动滑动条去改变颜色")
        # self.l1.setFont(QFont("Arial",16))
        # hbox.addWidget(self.l1)
        # self.s1 = QScrollBar()
        # self.s1.setMaximum(255)
        # self.s1.sliderMoved.connect(self.sliderval)
        # self.s2 = QScrollBar()
        # self.s2.setMaximum(255)
        # self.s2.sliderMoved.connect(self.sliderval)
        # self.s3 = QScrollBar()
        # self.s3.setMaximum(255)
        # self.s3.sliderMoved.connect(self.sliderval)
        # hbox.addWidget(self.s1)
        # hbox.addWidget(self.s2)
        # hbox.addWidget(self.s3)
        # self.setGeometry(300, 300, 300, 200)
        # self.setWindowTitle('QScrollBar 例子')
        # self.setLayout( hbox )

        hbox = QHBoxLayout()
        self.l0 = QLabel("拖动滑动条去改变颜色")
        self.l0.setFont(QFont("Arial", 16))
        hbox.addWidget(self.l0)

        self.s1 = QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderval)
        self.l1 = QLabel("红")
        self.l1.setFont(QFont("Arial", 12))

        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)
        self.l2 = QLabel("绿")
        self.l2.setFont(QFont("Arial", 12))

        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)
        self.l3 = QLabel("蓝")
        self.l3.setFont(QFont("Arial", 12))

        hbox.addWidget(self.s1)
        hbox.addWidget(self.l1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.l2)
        hbox.addWidget(self.s3)
        hbox.addWidget(self.l3)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QScrollBar 例子')
        self.setLayout(hbox)

    def sliderval(self):
        # print( self.s1.value(),self.s2.value(), self.s3.value() )
        palette = QPalette()
        c0 = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c0)
        self.l0.setPalette(palette)

        c1 = QColor(self.s1.value(), 0, 0, 255)
        palette.setColor(QPalette.Foreground, c1)
        self.l1.setPalette(palette)
        self.l1.setText(str(self.s1.value()))

        c2 = QColor(0, self.s2.value(), 0, 255)
        palette.setColor(QPalette.Foreground, c2)
        self.l2.setPalette(palette)
        self.l2.setText(str(self.s2.value()))

        c3 = QColor(0, 0, self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c3)
        self.l3.setPalette(palette)
        self.l3.setText(str(self.s3.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())
