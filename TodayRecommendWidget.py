#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtDeclarative import QDeclarativeView
import sys

class ModelObject(object):    
    def __init__(self, picName):
        self.picName = picName

class TestLineModel(QtCore.QAbstractListModel):
    PICNAME_ROLE = QtCore.Qt.UserRole + 1
    TEXT_ROLE = QtCore.Qt.UserRole + 2

    def __init__(self, parent=None):
        super(TestLineModel, self).__init__(parent)
        self._data = []
        
        # register roles (names one can use from qml)
        keys = {}
        keys[TestLineModel.PICNAME_ROLE] = 'picName'
        keys[TestLineModel.TEXT_ROLE] = 'text'
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
    def addPicName(self,picName):
        count = len(self._data)
        self.beginInsertRows(QtCore.QModelIndex(), count, count) # notify view about upcoming change        
        self._data.append(ModelObject(picName))
        self.endInsertRows() # notify view that change happened

    def addPicNameList(self,picNameList):
        count = len(self._data)
        self.beginInsertRows(QtCore.QModelIndex(), count, count) # notify view about upcoming change        
        for picName in picNameList:
            self._data.append(ModelObject(picName))
        self.endInsertRows() # notify view that change happened

    @QtCore.pyqtSlot()
    def remove(self):
        if len(self._data) > 0:
            position = len(self._data) -1
            self.beginRemoveRows(QtCore.QModelIndex(), position, position) # notify view about upcoming change
            self._data.pop()
            self.endRemoveRows() # notify view that change happened

    @QtCore.pyqtSlot()
    def onClicked(self):     
        print "onClicked picName"

class TodayRecommendWidget(QtGui.QMainWindow):
    '''今日推荐主界面'''
    def __init__(self, parent=None):
        super(TodayRecommendWidget, self).__init__()

        # self.view = QDeclarativeView()
        self.view = MyQDeclarativeView()
        self.view.setMouseTracking(True)

        ctxt = self.view.rootContext()


        listModel = TestLineModel()        
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
        listModel.addPicNameList([
            "pics/340126.jpg",
            "pics/381815.jpg",
            "pics/485180.jpg",
            "pics/1861261471.jpg",
            "pics/1669845108.jpg",
            "pics/2081821708.jpg",
            "pics/507984.jpg",
            ])
        ctxt.setContextProperty('myModel',listModel)

        self.view.setSource(QtCore.QUrl.fromLocalFile("todayRecommend.qml"))
        # self.view.setStyleSheet("""border:1px solid red""")
        self.rootObject = self.view.rootObject()
        self.rootObject.setProperty('globalWidth',1000)
        self.rootObject.setProperty('globalHeight',200)

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
        self.view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.view2.setResizeMode(QDeclarativeView.SizeRootObjectToView)

    def mouseMoveEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        # event.accept()

class MyQDeclarativeView(QDeclarativeView):
    def __init__(self, parent=None):
        super(MyQDeclarativeView, self).__init__()
        self.setMouseTracking(True)

    def mouseMoveEvent(self,event): 
        self.setCursor(QtCore.Qt.ArrowCursor)
        event.ignore()

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

