#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qt import *

class titleBar(QtGui.QWidget):

    def __init__(self,parent=None):
        super(titleBar,self).__init__(parent)

        self.title_label = QLabel()
        self.title_label.setStyleSheet("color:black")
        self.title_label.setText(u"虾米音乐")

        self.font = QtGui.QFont()
        self.font.setPixelSize(20)   #设置字号32,以像素为单位
        self.font.setFamily("SimSun")#设置字体，宋体
        self.font.setFamily(u"微软雅黑")
        #self.font.setWeight(20)     #设置字型,不加粗
        self.font.setBold(True)
        self.font.setItalic(False)   #设置字型,不倾斜
        self.font.setUnderline(False)#设置字型,无下划线

        self.title_label.setFont(self.font)

        self.close_button = QLabel()
        self.min_button   = QLabel()
        self.max_button   = QLabel()

        self.close_button.setPixmap(QPixmap("./img/orange.png"))
        self.min_button.setPixmap(QPixmap("./img/green.png"))
        self.max_button.setPixmap(QPixmap("./img/blue.png"))

        self.close_button.setFixedSize(15,15)
        self.min_button.setFixedSize(15,15)
        self.max_button.setFixedSize(15,15)

        self.close_button.setStyleSheet(""" 
                                    background:transparent
                                    """)
        self.min_button.setStyleSheet(""" 
                                    background:transparent
                                    """)
        self.max_button.setStyleSheet(""" 
                                    background:transparent
                                    """)
        self.title_label.setStyleSheet(""" 
                                    background:transparent;
                                    color:rgba(70,70,70,255);
                                    """)

        self.close_button.setScaledContents(True)
        self.min_button.setScaledContents(True)
        self.max_button.setScaledContents(True)

        self.searchLine = QtGui.QLineEdit()
        self.searchLine.setStyleSheet(""" 
                                    border:2px groove gray;
                                    border-radius:10px;
                                    text-align:center;
                                    padding:2px 10px;
                                    background:white;
                                    """)

        self.setStyleSheet('''
                        border-bottom: 0px solid rgb(170, 170, 170);
                        background: qlineargradient(spread:reflect,
                        x1:1, y1:1, x2:1, y1:1,
                        stop:1 rgba(250, 250, 250, 255),
                        stop:0 rgba(170, 170, 170, 255));
                    ''')

        #水平管理器
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.close_button,0,Qt.AlignVCenter)
        self.title_layout.addWidget(self.min_button  ,0,Qt.AlignVCenter)
        self.title_layout.addWidget(self.max_button  ,0,Qt.AlignVCenter)
        self.title_layout.addStretch()
        self.title_layout.addWidget(self.title_label,1,Qt.AlignCenter)
        self.title_layout.addWidget(self.searchLine)

        self.setLayout(self.title_layout)
        self.resize(1000, 60)
        self.setMaximumSize(1000, 60)
        self.setMinimumSize(1000, 60)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    TitleBar = titleBar()
    TitleBar.show()
    sys.exit(app.exec_())   