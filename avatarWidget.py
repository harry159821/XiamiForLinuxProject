#!usr/evn/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore
import sys

class avatarBtn(QtGui.QLabel):
    Clicked = QtCore.pyqtSignal()
    Entered = QtCore.pyqtSignal()
    Leaved = QtCore.pyqtSignal()
    Moved = QtCore.pyqtSignal(int,int)

    def __init__(self,parent=None):
        super(avatarBtn,self).__init__()
        self.setMouseTracking(True)
        self.showFlag = False
            
    def mouseReleaseEvent(self,event):
        self.Clicked.emit()
        
    def mouseMoveEvent(self,event):
        pass
        # self.Moved.emit(event.globalPos().x(),event.globalPos().y())
        
    def enterEvent(self,event):
        self.setPixmap(QtGui.QPixmap(r'./img/titleBar/avatar_button_hover.png'))
        self.Entered.emit()
   
    def leaveEvent(self,event):
        if not self.showFlag:
            self.setPixmap(QtGui.QPixmap(r'./img/titleBar/avatar_button_normal.png'))
            self.Leaved.emit()

class avatarWidget(QtGui.QWidget):
    def __init__(self):
        super(avatarWidget, self).__init__()

        self.avatar = QtGui.QLabel(self)
        self.avatar.setPixmap(QtGui.QPixmap(r'./img/titleBar/default_avatar.png'))
        self.avatar.setScaledContents(True)
        self.avatar.setMaximumSize(27,27)

        self.button = avatarBtn()
        self.button.setParent(self)
        # self.button.setMinimumSize(30,30)
        self.button.setMaximumSize(28*1.39,28)
        self.button.setScaledContents(True)
        self.button.setPixmap(QtGui.QPixmap(r'./img/titleBar/avatar_button_normal.png'))


        self.avatar.move(0,10)
        self.button.move(0,10)
        # self.resize(27*1.39,27)

        self.pop_menu = QtGui.QMenu();

        self.action_name = QtGui.QAction(self)
        self.action_size = QtGui.QAction(self)
        self.action_type = QtGui.QAction(self)
        self.action_date = QtGui.QAction(self)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.button.Clicked.connect(self.clickedFun)
        self.pop_menu.aboutToHide.connect(self.aboutToHide)
        self.pop_menu.aboutToShow.connect(self.aboutToShow)
    
    def aboutToShow(self):
        self.button.setPixmap(QtGui.QPixmap(r'./img/titleBar/avatar_button_down.png'))
        self.button.showFlag = True

    def aboutToHide(self):
        self.button.setPixmap(QtGui.QPixmap(r'./img/titleBar/avatar_button_normal.png'))
        self.button.showFlag = False

    def clickedFun(self):
        # print self.frameGeometry().x(),self.frameGeometry().y()
        print self.button.frameRect()
        self.pop_menu.clear() # 清除原有菜单
        self.pop_menu.addAction(self.action_name)
        self.pop_menu.addAction(self.action_size)
        self.pop_menu.addAction(self.action_type)
        self.pop_menu.addAction(self.action_date)

        self.pop_menu.exec_(QtCore.QPoint(self.frameGeometry().x()+56,self.frameGeometry().y()+57))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = avatarWidget()
    w.show()
    sys.exit(app.exec_())        