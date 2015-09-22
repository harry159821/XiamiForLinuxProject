#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

# class Label(QtGui.QLabel):
#     def __init__(self,flag):
#         super(Label, self).__init__()
#         self.setText(u"测试")
#         self.setProperty("flag",flag) # 有Flag就变色
#         self.setFixedHeight(40)

class Label(QtGui.QWidget):
    def __init__(self,flag):
        super(Label, self).__init__()
        self.font = QtGui.QFont()
        self.font.setPixelSize(14)
        self.font.setFamily(u"微软雅黑")
        self.font.setBold(True)
        # self.font.

        if flag:
            self.setStyleSheet("background:rgb(37,70,79);")
        # self.resize(150,40)

        self.label = QtGui.QLabel(self)
        self.label.setText(u"测试")
        self.label.move(50,5)
        self.label.setFont(self.font)
        # self.label.setStyleSheet("{color:r:}")
        self.label2 = QtGui.QLabel(self)
        self.label2.setText(u"测试")
        self.label2.move(50,20)
        self.font.setPixelSize(10)
        self.font.setBold(False)
        self.label2.setFont(self.font)
        # self.label2.setFixedHeight(7)

        self.setProperty("flag",flag) # 有Flag就变色
        self.setFixedHeight(40)

class TreeWidget(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(TreeWidget,self).__init__()

        self.tree = QtGui.QTreeWidget()
        for i in range(1,10):
            QtGui.QTreeWidgetItem(self.tree) # 生成十行控件

        self.tree.setItemWidget(self.tree.topLevelItem(0),0,Label(False))
        self.tree.setItemWidget(self.tree.topLevelItem(1),0,Label(True))
        self.tree.setItemWidget(self.tree.topLevelItem(2),0,Label(False))
        self.tree.setItemWidget(self.tree.topLevelItem(3),0,Label(True))

        self.tree.setItemWidget(self.tree.topLevelItem(4),0,QtGui.QPushButton("Push ME"))
        self.tree.setItemWidget(self.tree.topLevelItem(5),0,QtGui.QPushButton("Push ME"))
        self.tree.setItemWidget(self.tree.topLevelItem(6),0,QtGui.QPushButton("Push ME"))
        self.tree.setItemWidget(self.tree.topLevelItem(7),0,QtGui.QPushButton("Push ME"))

        self.tree.setHeaderHidden(True)     # 隐藏头部
        self.tree.setRootIsDecorated(False) # 去除根结点缩进,去掉虚线边框
        self.tree.setFocusPolicy(QtCore.Qt.NoFocus) # 去除虚线
        self.setCentralWidget(self.tree)

        self.tree.setStyleSheet('''
            QTreeWidget {
                background-color:rgb(77,135,139);
            }
            Label[flag="true"] { 
                background:rgb(37,70,79);
                border-right:5px solid orange;
            }
            ''')

        return
        #设置列数
        #self.tree.setColumnCount(1)
        #设置头部
        #self.tree.setHeaderLabels(['Key'])
        #隐藏头部
        self.tree.setHeaderHidden(True)
        #展开结点,无效
        #self.tree.expandAll()
        #去除根结点缩进,去掉虚线边框
        self.tree.setRootIsDecorated(False)
        #列宽?两列以上起作用
        #self.tree.setColumnWidth(10,100)
        #单选
        self.tree.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        #可滑动多选
        #self.tree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        #self.tree.setSelection(QtCore.QRect(1,2,3,4),QtGui.QItemSelectionModel.Current)

        #Failed Set
        #selection = QtGui.QItemSelection()
        #selection = self.tree.selectionModel.selection()
        #selection.select(topLeft,bottomRight)
        #self.tree(topLeft,QItemSelectionModel.ClearAndSelect|QItemSelectionModel.Rows)

        #Plastique Style
        #self.tree.setStyle(QtGui.QStyleFactory.create("plastique"));
        #选中整行
        self.tree.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #只选单个Item
        #self.tree.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        #缩进
        #self.tree.setIndentation(10)
        #设置选中的选项整行获得焦点
        self.tree.setAllColumnsShowFocus(True)
        self.tree.hideColumn(1)

        #去除虚线
        self.tree.setFocusPolicy(QtCore.Qt.NoFocus)

        root = QtGui.QTreeWidgetItem(self.tree)
        root.setText(0,u'发现')
        #ICON
        #root.setIcon(0, QtGui.QIcon('header.png'))
        self.tree.expandItem(root)

        #交替颜色
        #self.tree.setAlternatingRowColors(True)

        child1 = QtGui.QTreeWidgetItem(root)
        child1.setText(0,u'今日推荐')
        child1.setIcon(0,QtGui.QIcon('img/tree/section_today_recommends.png'))

        child2 = QtGui.QTreeWidgetItem(root)
        child2.setText(0,u'虾小米精选')
        child2.setIcon(0,QtGui.QIcon('img/tree/section_suggest_collects.png'))

        child3 = QtGui.QTreeWidgetItem(root)
        child3.setText(0,u'音乐排行榜') 
        child3.setIcon(0,QtGui.QIcon('img/tree/section_top_songs.png'))

        child4 = QtGui.QTreeWidgetItem(root)
        child4.setText(0,u'音乐电台')
        child4.setIcon(0,QtGui.QIcon('img/tree/section_radios.png'))

        child5 = QtGui.QTreeWidgetItem(root)
        child5.setText(0,u'猜你喜欢')
        child5.setIcon(0,QtGui.QIcon('img/tree/section_guess_you_like.png'))
                        
        root2 = QtGui.QTreeWidgetItem(self.tree)
        root2.setText(0,u'我的音乐')
        self.tree.expandItem(root2)

        child6 = QtGui.QTreeWidgetItem(root2)
        child6.setText(0,u'本地音乐')
        child6.setIcon(0,QtGui.QIcon('img/tree/section_itunes.png'))

        child7 = QtGui.QTreeWidgetItem(root2)
        child7.setText(0,u'播放记录')
        child7.setIcon(0,QtGui.QIcon('img/tree/section_playlogs.png'))

        child8 = QtGui.QTreeWidgetItem(root2)
        child8.setText(0,u'联想歌单')
        child8.setIcon(0,QtGui.QIcon('img/tree/section_more_like.png'))

        child9 = QtGui.QTreeWidgetItem(root2)
        child9.setText(0,u'我的收藏')
        child9.setIcon(0,QtGui.QIcon('img/tree/section_favorites.png'))

        child10 = QtGui.QTreeWidgetItem(root2)
        child10.setText(0,u'精选集')
        child10.setIcon(0,QtGui.QIcon('img/tree/section_collects.png'))

        child11 = QtGui.QTreeWidgetItem(root2)
        child11.setText(0,u'离线音乐')
        child11.setIcon(0,QtGui.QIcon('img/tree/section_offline_music.png'))
        child11.setProperty("ter","test")

        self.setCentralWidget(self.tree)
        self.resize(200,450)


        self.tree.setStyleSheet('''
        QTreeView {
            selection-background-color:rgb(255,0,0,100);
        }

        QTreeView::item:selected
        {
            background-color:rgb(255,0,0,100);
        }
            ''')

class MyTree(QtGui.QTreeWidget):
    """docstring for MyTree"""
    def __init__(self, parent=None):
        super(MyTree, self).__init__()

    def drawRow(self,painter,option,index):
        painter.save()
        brush = QtGui.QBrush(QtGui.QColor(255,240,180))
        painter.fillRect(option.rect,brush)
        painter.restore()
        QtGui.QTreeWidget.drawRow(self,painter,option,index)

app = QtGui.QApplication(sys.argv)
testWidget = TreeWidget()
testWidget.show()
app.exec_()



'''
QTreeWidget Signals

void currentItemChanged (QTreeWidgetItem *,QTreeWidgetItem *)
void itemActivated (QTreeWidgetItem *,int)
void itemChanged (QTreeWidgetItem *,int)
void itemClicked (QTreeWidgetItem *,int)
void itemCollapsed (QTreeWidgetItem *)
void itemDoubleClicked (QTreeWidgetItem *,int)
void itemEntered (QTreeWidgetItem *,int)
void itemExpanded (QTreeWidgetItem *)
void itemPressed (QTreeWidgetItem *,int)
void itemSelectionChanged ()
'''