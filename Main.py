#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtDeclarative import QDeclarativeView
import songTable
import TodayRecommendWidget
import mainWindows

'''
Xiami For Linux Project
'''
class XiamiPlayer(object):
    def __init__(self):
        super(XiamiPlayer, self).__init__()
        self.app = QtGui.QApplication(sys.argv)




        
        self.testWidget = mainWindows.MainWindow()
        self.testWidget.show()        
        # Run
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    xiamiPlayer = XiamiPlayer()
