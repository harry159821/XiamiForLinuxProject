#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore

class TreeWidget(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(TreeWidget,self).__init__()

		self.tree = QtGui.QTreeWidget()
		#设置列数
		#self.tree.setColumnCount(1)
		#设置头部
		#self.tree.setHeaderLabels(['Key'])
		#隐藏头部
		self.tree.setHeaderHidden(True)
		#展开结点,无效
		self.tree.expandAll()
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
		#self.tree.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		#只选单个Item
		#self.tree.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
		#缩进
		self.tree.setIndentation(10)
		#设置选中的选项整行获得焦点
		#self.tree.setAllColumnsShowFocus(True)
		self.tree.hideColumn(1)

		root = QtGui.QTreeWidgetItem(self.tree)
		root.setText(0,u'发现')
		#ICON
		#root.setIcon(0, QtGui.QIcon('header.png'))
		self.tree.expandItem(root)

#		self.setStyleSheet("""
#						QTreeWidget{
#						show-decoration-selected:1;
#						}
#						""")

		self.tree.setStyleSheet("""

QTreeView {
	alternate-background-color: yellow;
	background:url(./gray2.png);
}

QTreeWidget::item{
	height:32px;
}

QTreeView::item:hover {
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
	border: 1px solid #bfcde4;
}

QTreeView::item:selected {
	background-color:rgb(0,0,0,100)
	border: 1px solid #567dbc;
}

QTreeView::branch {
	image:none;
}

QTreeView::item:selected:active{
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);
}

QTreeView::item:selected:!active {
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);
}

						""")

		child1 = QtGui.QTreeWidgetItem(root)
		child1.setText(0,u'今日推荐')
		child1.setIcon(0,QtGui.QIcon('section_today_recommends.png'))

		child2 = QtGui.QTreeWidgetItem(root)
		child2.setText(0,u'虾小米精选')
		child2.setIcon(0,QtGui.QIcon('section_suggest_collects.png'))

		child3 = QtGui.QTreeWidgetItem(root)
		child3.setText(0,u'音乐排行榜')
		child3.setIcon(0,QtGui.QIcon('section_top_songs.png'))

		child4 = QtGui.QTreeWidgetItem(root)
		child4.setText(0,u'音乐电台')
		child4.setIcon(0,QtGui.QIcon('section_radios.png'))

		child5 = QtGui.QTreeWidgetItem(root)
		child5.setText(0,u'猜你喜欢')
		child5.setIcon(0,QtGui.QIcon('section_guess_you_like.png'))
						
		root2 = QtGui.QTreeWidgetItem(self.tree)
		root2.setText(0,u'我的音乐')
		self.tree.expandItem(root2)

		child6 = QtGui.QTreeWidgetItem(root2)
		child6.setText(0,u'本地音乐')
		child6.setIcon(0,QtGui.QIcon('section_itunes.png'))

		child7 = QtGui.QTreeWidgetItem(root2)
		child7.setText(0,u'播放记录')
		child7.setIcon(0,QtGui.QIcon('section_playlogs.png'))

		child8 = QtGui.QTreeWidgetItem(root2)
		child8.setText(0,u'联想歌单')
		child8.setIcon(0,QtGui.QIcon('section_more_like.png'))

		child9 = QtGui.QTreeWidgetItem(root2)
		child9.setText(0,u'我的收藏')
		child9.setIcon(0,QtGui.QIcon('section_favorites.png'))

		child10 = QtGui.QTreeWidgetItem(root2)
		child10.setText(0,u'精选集')
		child10.setIcon(0,QtGui.QIcon('section_collects.png'))

		child11 = QtGui.QTreeWidgetItem(root2)
		child11.setText(0,u'离线音乐')
		child11.setIcon(0,QtGui.QIcon('section_offline_music.png'))

		self.setCentralWidget(self.tree)
		self.resize(200,450)

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