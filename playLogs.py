#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore,Qt
import songTable

class SongLogs(songTable.SongTable):
    def __init__(self):
        super(SongLogs, self).__init__()  


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    songTable = SongLogs()
    songTable.show()
    sys.exit(app.exec_())