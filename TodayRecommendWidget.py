#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtDeclarative import QDeclarativeView
from PyQt4 import QtDeclarative
import sys

class ModelObject(object):    
    def __init__(self, picName,text=None):
        self.picName = picName
        self.text = text

class TestLineModel(QtCore.QAbstractListModel):
    PICNAME_ROLE = QtCore.Qt.UserRole + 1
    TEXT_ROLE = QtCore.Qt.UserRole + 2

    def __init__(self, parent=None):
        super(TestLineModel, self).__init__(parent)
        self._data = []
        
        # register roles (names one can use from qml)
        keys = {}
        keys[TestLineModel.PICNAME_ROLE] = 'picName'
        keys[TestLineModel.TEXT_ROLE] = 'picText'
        self.setRoleNames(keys)
        
    def rowCount(self, index):
        return len(self._data)
        
    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._data):
            return None
            
        line = self._data[index.row()]
        
        if role == TestLineModel.PICNAME_ROLE:
            return line.picName
        elif role == TestLineModel.TEXT_ROLE:
            return line.text
        else:
            return None
          
    @QtCore.pyqtSlot()
    def add(self):
        count = len(self._data)        
        self.beginInsertRows(QtCore.QModelIndex(), count, count) # notify view about upcoming change        
        self._data.append(ModelObject("pics/340126.jpg"))
        self.endInsertRows() # notify view that change happened

    @QtCore.pyqtSlot()
    def addPicName(self,picName,text=None):
        count = len(self._data)
        self.beginInsertRows(QtCore.QModelIndex(), count, count) # notify view about upcoming change        
        self._data.append(ModelObject(picName,text))
        self.endInsertRows() # notify view that change happened

    def addPicNameList(self,picNameList):
        count = len(self._data)
        self.beginInsertRows(QtCore.QModelIndex(), count, count) # notify view about upcoming change        
        for picName,text in picNameList:
            self._data.append(ModelObject(picName,text))
        self.endInsertRows() # notify view that change happened

    @QtCore.pyqtSlot()
    def remove(self):
        if len(self._data) > 0:
            position = len(self._data) -1
            self.beginRemoveRows(QtCore.QModelIndex(), position, position) # notify view about upcoming change
            self._data.pop()
            self.endRemoveRows() # notify view that change happened

    # @QtCore.pyqtSlot()
    def onClicked(self,name):
        print "onClicked ",name

    def findIndex(self,picName):
        '''定位'''
        for i in range(0,len(self._data)):
            if self._data[i].picName == picName:
                return i

class QmlLabel(QtDeclarative.QDeclarativeItem):
    def __init__(self, parent):
        super(QmlLabel, self).__init__()
        self.mLabel = QtGui.QLabel(u"Label")
        self.mProxy = QtGui.QGraphicsProxyWidget(self)
        self.mProxy.setWidget(self.mLabel)
        
    def selText(self,text):
        self.mLabel.setText(text)

    def text(self):
        return self.mLabel.text()

class TodayRecommendWidget(QtGui.QMainWindow):
    '''今日推荐主界面'''
    def __init__(self, parent=None):
        super(TodayRecommendWidget, self).__init__()

        # self.view = QDeclarativeView()
        self.view = MyQDeclarativeView()
        self.view.setMouseTracking(True)

        ctxt = self.view.rootContext()


        self.listModel = TestLineModel()        
        # add some data to the model
        # listModel.addPicName("pics/340126.jpg")
        # listModel.addPicName("pics/340126.jpg")
        # listModel.addPicName("pics/340126.jpg")
        # listModel.addPicName("pics/340126.jpg")
        # listModel.addPicName("pics/340126.jpg")
        # listModel.add()
        # listModel.add()
        # listModel.add()
        # listModel.add()
        # listModel.add()
        self.listModel.addPicNameList([
                ["pics/340126.jpg"    ,"Sample Text"],
                ["pics/381815.jpg"    ,"Sample Text"],
                ["pics/485180.jpg"    ,"Sample Text"],
                ["pics/1861261471.jpg","Sample Text"],
                ["pics/1669845108.jpg","Sample Text"],
                ["pics/2081821708.jpg","Sample Text"],
                ["pics/507984.jpg"    ,"Sample Text"],
            ])
        ctxt.setContextProperty('myModel',self.listModel)

        self.view.setSource(QtCore.QUrl.fromLocalFile("todayRecommend.qml"))
        # self.view.setStyleSheet("""border:1px solid red""")
        self.rootObject = self.view.rootObject()
        self.rootObject.setProperty('globalWidth',1000)
        self.rootObject.setProperty('globalHeight',180)
        self.rootObject.sendClicked.connect(self.onClicked)

        self.view2 = MyQDeclarativeView()
        self.view2.setSource(QtCore.QUrl.fromLocalFile("todayRecommendBottom.qml"))
        # self.view2.setStyleSheet("""border:1px solid red""")

        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addWidget(self.view)
        self.mainLayout.addWidget(self.view2)
        self.mainLayout.setSpacing(0)
        # left top right bottom
        self.mainLayout.setContentsMargins(0,0,0,0)

        # 设置部件比例
        self.mainLayout.setStretch(0,5)
        self.mainLayout.setStretch(1,3)

        self.mainWidget = QtGui.QWidget()
        self.mainWidget.setMouseTracking(True)
        self.setStyleSheet("""
            QDeclarativeView
            {
                border-top:     0px solid #adadad;
                border-left:    0px solid #919191;
                border-right:   1px solid #919191;
                border-bottom:  0px solid #919191;
            }
            """)
        self.setCentralWidget(self.mainWidget)
        self.mainWidget.setLayout(self.mainLayout)

        # print self.size().height()/4

        # 使得QML窗口随父窗口大小改变而改变
        # ............令人无语的问题，加上自调整后会上下滚动
        # 试着在 ResizeEvent 重置吧
        self.view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.view2.setResizeMode(QDeclarativeView.SizeRootObjectToView)

    def onClicked(self,picName):
        picName = picName.toUtf8().data()
        pos = self.listModel.findIndex(picName)
        index = self.rootObject.currentIndex()
        # 判断点击位置距离中心的距离并滚动所点击项到中间
        l = []
        for i in range(0,len(self.listModel._data)):
            l.append(i)
        length = len(l)
        tmpl = 3*l
        currentList = []
        for i in [-2,-1,0,1,2]:
            currentList.append(tmpl[index+i+length])
        pos = currentList.index(pos)-2
        if pos>0:
            for i in range(0,pos):
                self.rootObject.incrementCurrentIndex()     
        elif pos<0:
            for i in range(0,-pos):
                self.rootObject.decrementCurrentIndex()

    def decrementCurrentIndex(self):
        self.rootObject.decrementCurrentIndex()
        self.repaint()
        self.rootObject.update()

    def mouseMoveEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        event.ignore()

    def wheelEvent(self,event):
        # self.setCursor(QtCore.Qt.ArrowCursor)
        print "mouseWheelEvent"
        self.rootObject.decrementCurrentIndex()
        event.accept()

class MyQDeclarativeView(QDeclarativeView):
    def __init__(self, parent=None):
        super(MyQDeclarativeView, self).__init__()
        self.setMouseTracking(True)

    def enterEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)

    # def mouseMoveEvent(self,event): 
    #     self.setCursor(QtCore.Qt.ArrowCursor)
    #     event.accept()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    testWidget = TodayRecommendWidget()
    testWidget.resize(850,550)
    testWidget.show()
    sys.exit(app.exec_())

'''
# ------------------------------------------------------------------------------------------
class TodayRecommendDataObject(QtCore.QObject):
    picNameChanged = QtCore.pyqtSignal()
    def __init__(self, picName):
        super(TodayRecommendDataObject, self).__init__()
        self._picName = picName

    @QtCore.pyqtProperty(str, notify=picNameChanged)
    def picName(self):
        return self._picName

    @picName.setter
    def picName(self, picName):
        if self._picName != picName:
            self._picName = picName
            self.picNameChanged.emit()
# ------------------------------------------------------------------------------------------
        # stringList = [  TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/340126.jpg"),
        #                 TodayRecommendDataObject("pics/381815.jpg"),]
        # ctxt.setContextProperty('myModel',stringList)
        # ctxt.setContextProperty('myModel',SimpleListModel(['Red1','Red2','Yellow']))
# ------------------------------------------------------------------------------------------    
'''

