#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys,random,time
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtDeclarative import QDeclarativeView

class RenderCircleWindows(QtGui.QMainWindow):
    def __init__(self):
        super(RenderCircleWindows, self).__init__()
        self.widget = RenderCircleWidget()
        self.setCentralWidget(self.widget)
        self.resize(500,400)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint|QtCore.Qt.FramelessWindowHint)
        
class RenderCircleWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        super(RenderCircleWidget, self).__init__()
        self.resize(500,400)        
        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        
        self.colorClass = ColorClass()
        self.colorClass.random()

        # self.thread = RenderCircleThread()
        # self.thread.change.connect(self.render)
        # self.thread.render(self)
        
        self.posx = 0

        self.color = QtGui.QColor(0,0,0)

        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.render)
        self.time.start(3)        

        self.subColorList = []
        for i in range(1,50):
            self.subColorList.append(SubColorClass(170,40))

    def render(self):             
        # self.repaint()
        self.update()

    def paintEvent(self,event):
        painter = QtGui.QPainter(self)       
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # painter.setBrush(QtGui.QBrush(QtGui.QColor(235,45,211),QtCore.Qt.SolidPattern))
        # painter.setPen(QtGui.QPen(QtGui.QColor(218,92,202),9))
        # painter.drawEllipse(20,20,100,100)

        # painter = QtGui.QPainter(self)
        # painter.drawLine(100,10,100,200)

        # self.posx = 0
        # for i in range(1,500):
        #     self.posx += 1
        #     self.colorClass.change(1)
        #     color = QtGui.QColor(self.colorClass.r,self.colorClass.g,self.colorClass.b)
        #     painter.setPen(QtGui.QPen(color,9))
        #     painter.drawLine(self.posx,0,self.posx,400)

        # SubCircle
        for subColor in self.subColorList:
            subColor.change()
            color2 = QtGui.QColor(  subColor.radioSpeed*subColor.color.r,
                                    subColor.radioSpeed*subColor.color.g,
                                    subColor.radioSpeed*subColor.color.b)
            color = QtGui.QColor(   subColor.radioSpeed+subColor.color.r,
                                    subColor.radioSpeed+subColor.color.g,
                                    subColor.radioSpeed+subColor.color.b)            
            painter.setPen(QtGui.QPen(color2,subColor.radio*0.05))
            painter.setBrush(QtGui.QBrush(color,QtCore.Qt.SolidPattern))
            painter.drawEllipse(subColor.x,subColor.y,subColor.radio,subColor.radio)

class RenderCircleThread(QtCore.QThread):
    change = QtCore.pyqtSignal()
    def __init__(self):
        super(RenderCircleThread, self).__init__()

    def render(self,parent):
        self.parent = parent
        self.run()

    def run(self):
        for i in range(1,1000):
            self.parent.colorClass.change(1)
            # print self.parent.colorClass.color()
            # self.parent.repaint()
            # time.sleep(1)
            self.change.emit()

class SubColorClass(object):
    def __init__(self,Ox=0,Oy=0):
        super(SubColorClass, self).__init__()
        self.color = ColorClass()
        self.radio = 5
        self.radioSpeed = random.random()*0.7
        self.Ox,self.Oy = Ox,Oy+10
        self.x,self.y = Ox,Oy+10
        self.XDirection = 2*(random.random()-0.5)*0.1
        self.YDirection = 2*(random.random()-0.5)*0.1
        self.Opacity = random.random()/4 +0.75
        self.Opacity = random.random()

    def clear(self):
        self.count = 0
        self.radio = 5
        self.x,self.y = self.Ox,self.Oy
        self.XDirection = 2*(random.random()-0.5)
        self.YDirection = 2*(random.random()-0.5)

    def change(self):
        self.radio += self.radioSpeed
        self.color.change(1)
        self.x += self.XDirection
        self.y += abs(self.YDirection)
        if self.radio > 80:
            self.clear()

class ColorClass(object):
    def __init__(self):
        super(ColorClass, self).__init__()
        self.r,self.g,self.b = 255,0,0
    
    def color(self):
        return self.r,self.g,self.b

    def random(self):
        for i in xrange(1,int(random.random()*1000)):
            self.change(1)
        print self.r,self.g,self.b," ",self.level()

    def level(self):
        if self.g <= 0:
            if self.b < 255:
                return 1
            if 0 < self.r <= 255:
                return 2
        if self.r <= 0:
            if self.g < 255:
                return 3
            if 0 < self.b <= 255:
                return 4
        if self.b <= 0:
            if self.r < 255:
                return 5
            if 0 < self.g <= 255:
                return 6

    def change(self,value=5):
        level = self.level()
        if level == 1:
            self.b += value
        elif level == 2:
            self.r -= value
        elif level == 3:
            self.g += value
        elif level == 4:
            self.b -= value
        elif level == 5:
            self.r += value
        else:
            self.g -= value
        if self.r < 0:self.r = 0
        if self.g < 0:self.g = 0
        if self.b < 0:self.b = 0
        if self.r > 255:self.r = 255
        if self.g > 255:self.g = 255
        if self.b > 255:self.b = 255

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    RenderCircleWidget = RenderCircleWindows()
    RenderCircleWidget.show()
    sys.exit(app.exec_())

    # color = ColorClass()
    # color.random()
