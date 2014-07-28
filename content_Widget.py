#!/usr/bin/python
# -*- coding:utf-8 -*-
import os,sys
from PyQt4 import QtGui,QtCore,Qt
'''
Xiami For Linux Project
'''
class ContentWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(ContentWidget,self).__init__()
		self.resize(650,560)

		self.List = QtGui.QListWidget()
		self.List.setShortcutEnabled(True)
		item = ['1','2','3','4']
		listItem = []
		for i in item:
			listItem.append(QtGui.QListWidgetItem(i))
		for i in listItem:
			self.List.addItem(i)
		#距离问题有待
		self.List.resize(500,560)
		#self.List.setFixedSize(450,560)
		#自适应窗口宽度
		self.List.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		#去除难看的边框
		self.List.setStyleSheet("""
						border: 0px;
						""")

		# win失败，效果太烂
		# self.List.setFrameStyle(QtGui.QFrame.WinPanel)
		# self.List.setFrameShadow(QtGui.QFrame.Sunken)
		# self.List.setLineWidth(3)
		# self.List.setMidLineWidth(3)

		#self.makeBackgroundWhite()

		#主分界框架
		self.main_splitter = QtGui.QSplitter()
		#任意伸展自适应
		self.main_splitter.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
		#设置方向
		self.main_splitter.setOrientation(QtCore.Qt.Vertical)
		#分界线宽度
		self.main_splitter.setHandleWidth(1)
		#设置灰度
		self.main_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")
		#self.main_splitter.setStyleSheet("QSplitter.handle{background:gray}")

		self.content_splitter = QtGui.QSplitter()
		self.content_splitter.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
		self.content_splitter.setOrientation(QtCore.Qt.Horizontal)
		self.content_splitter.setHandleWidth(1)
		self.content_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")

		self.a = TreeWidget()
		self.b = QtGui.QWidget()

		self.titlebar = titleBar()
		self.titlebar.resize(1000, 50)
		self.titlebar.setFixedSize(1000, 50)
		# self.titlebar.setStyleSheet('''
		# 				border: 1px;
		# 				background: qlineargradient(spread:reflect,
		# 				x1:1, y1:1, x2:1, y1:1,
		# 				stop:1 rgba(250, 250, 250, 255),
		# 				stop:0 rgba(170, 170, 170, 255));
		# 			''')

		self.ControlBar = controlBar()
		self.ControlBar.resize(1000, 60)
		self.ControlBar.setFixedSize(1000, 60)

		self.a.tree.resize(200,560)
		self.a.tree.setFixedSize(200,560)

		self.content_splitter.addWidget(self.a.tree)
		self.content_splitter.addWidget(self.List)

		self.main_splitter.addWidget(self.titlebar)
		self.main_splitter.addWidget(self.content_splitter)
		self.main_splitter.addWidget(self.ControlBar)

		# for i in range(self.main_splitter.count()):
		# 	handle = QtGui.QSplitterHandle(QtCore.Qt.Horizontal, self.main_splitter)
		# 	self.main_splitter.handle(i)
		# 	handle.setEnabled(False)

		self.main_layout = QtGui.QHBoxLayout()
		self.main_layout.addWidget(self.main_splitter)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0,0,0,0)
		self.setLayout(self.main_layout)
		self.window_attribute()

	# def makeBackgroundWhite(self):
	# 	'''设置窗口背景为白色'''
	# 	self.palette = QtGui.QPalette()
	# 	self.palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(QtCore.Qt.white))
	# 	self.setPalette(self.palette)
	# 	self.setAutoFillBackground(True)

	def window_attribute(self):
		if os.name != 'nt':
			#隐藏窗口边框、背景、任务栏
			self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.X11BypassWindowManagerHint | QtCore.Qt.SplashScreen)           
		else:
			self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)# | QtCore.Qt.Tool)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
		self.setMouseTracking(True)
		#窗口透明度
		#self.setWindowOpacity(0.9)

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QtGui.QApplication.postEvent(self, QtCore.QEvent(174))
			event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

class OptionItem(QtGui.QLabel):
	Clicked = QtCore.pyqtSignal(str)
	Entered = QtCore.pyqtSignal(str)
	Leaved = QtCore.pyqtSignal(str)
	'''已废弃?'''
	def __init__(self,parent=None,name=None,title=None):
		super(Item,self).__init__()
		self.name = name
		self.icon = QLabel(self)
		self.icon.move(10,10)
		self.icon.setPixmap('./'+self.name+'_normal.png')

		self.title = title
		self.title_label = QLabel(self)
		self.title_label.move(20,10)
		self.title_label.setText(self.title)

	def mouseReleaseEvent(self,event):
		self.Clicked.emit(self.name)

	def enterEvent(self,event):
		self.icon.setPixmap('./'+self.name+'_hover.png')
		self.setStyleSheet('''
						background:white;
						''')
		self.title_label.setStyleSheet("""
						color: rgb(255, 255, 255);
						""")
		self.Entered.emit(self.name)

	def leaveEvent(self,event):
		self.icon.setPixmap('./'+self.name+'_normal.png')
		self.setStyleSheet('''
						background:black;
						''')
		self.title_label.setStyleSheet("""
						color: rgb(0, 0, 0);
						""")		
		self.Leaved.emit(self.name)

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

		self.setStyleSheet("""
						border: 0px;
						""")

		self.tree.setStyleSheet("""

		QTreeView {
			alternate-background-color: yellow;
			background:url(./gray2.png);
			border: 0px;
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

		#self.setCentralWidget(self.tree)
		#self.resize(200,450)

class titleBar(QtGui.QMainWindow):

	def __init__(self,parent=None):
		super(titleBar,self).__init__(parent)

		self.title_label = QtGui.QLabel()
		self.title_label.setStyleSheet("color:black")
		self.title_label.setText(u"虾米音乐")
		self.title_label.setText(u"Xiami For Linux Project")

		self.font = QtGui.QFont()
		self.font.setPixelSize(20)   #设置字号32,以像素为单位
		self.font.setFamily("SimSun")#设置字体，宋体
		self.font.setFamily(u"微软雅黑")
		#self.font.setWeight(20)     #设置字型,不加粗
		self.font.setBold(True)
		self.font.setItalic(False)   #设置字型,不倾斜
		self.font.setUnderline(False)#设置字型,无下划线

		self.title_label.setFont(self.font)

		self.close_button = QtGui.QPushButton()
		self.min_button   = QtGui.QPushButton()
		self.max_button   = QtGui.QPushButton()

		self.close_button.setIcon(QtGui.QIcon("./img/orange.png"))
		self.min_button.setIcon(QtGui.QIcon("./img/green.png"))
		self.max_button.setIcon(QtGui.QIcon("./img/blue.png"))		

		self.close_button.setFixedSize(15,15)
		self.min_button.setFixedSize(15,15)
		self.max_button.setFixedSize(15,15)

		self.close_button.setStyleSheet(""" 
									background:transparent;
									""")
		self.min_button.setStyleSheet(""" 
									background:transparent;
									""")
		self.max_button.setStyleSheet(""" 
									background:transparent;
									""")
		self.title_label.setStyleSheet(""" 
									background:transparent;
									color:rgba(70,70,70,255);
									""")

		self.close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)

		self.searchLine = QtGui.QLineEdit()
		self.searchLine.setStyleSheet("""
									border:2px groove gray;
									border-radius:10px;
									text-align:center;
									padding:2px 10px;
									background:white;
									""")

		self.setStyleSheet('''
		QWidget
		{
			border-bottom: 0px solid rgb(170, 170, 170);
			background: qlineargradient(spread:reflect,
			x1:1, y1:1, x2:1, y1:1,
			stop:1 rgba(250, 250, 250, 255),
			stop:0 rgba(170, 170, 170, 255));
		}	
					''')

		#水平管理器
		self.title_layout = QtGui.QHBoxLayout()
		self.title_layout.addWidget(self.close_button,0,QtCore.Qt.AlignVCenter)
		self.title_layout.addWidget(self.min_button  ,0,QtCore.Qt.AlignVCenter)
		self.title_layout.addWidget(self.max_button  ,0,QtCore.Qt.AlignVCenter)
		self.title_layout.addStretch()
		self.title_layout.addWidget(self.title_label,1,QtCore.Qt.AlignCenter|QtCore.Qt.AlignHCenter)
		self.title_layout.addWidget(self.searchLine)

		self.widget = QtGui.QWidget()
		self.setCentralWidget(self.widget)
		self.widget.setLayout(self.title_layout)
		#self.setLayout(self.title_layout)
		#self.resize(1000, 60)
		#self.setMaximumSize(1000, 60)
		#self.setMinimumSize(1000, 60)

class controlBar(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(controlBar,self).__init__(parent)
		self.setAutoFillBackground(True)

		#palette = QtGui.QPalette()
		#palette.setBrush(QtGui.QPalette.Background,
		#	QtGui.QBrush(QtGui.QPixmap("bottom_bar_bg.tiff")))
		#self.setPalette(palette);

		self.font = QtGui.QFont()
		self.font.setPixelSize(20)   #设置字号32,以像素为单位
		self.font.setFamily("SimSun")#设置字体，宋体
		self.font.setFamily(u"微软雅黑")
		#self.font.setWeight(20)     #设置字型,不加粗
		self.font.setBold(True)
		self.font.setItalic(False)   #设置字型,不倾斜
		self.font.setUnderline(False)#设置字型,无下划线

		self.resize(1000, 60)

		self.playPreBtn = QtGui.QPushButton()
		self.playPreBtn.setObjectName('playPreBtn')
		self.playOrPauseBtn = QtGui.QCheckBox()
		self.playOrPauseBtn.setObjectName('playOrPauseBtn')
		self.playNextBtn = QtGui.QPushButton()
		self.playNextBtn.setObjectName('playNextBtn')

		self.favSongCheckBox = QtGui.QCheckBox()
		self.bufferSlider = QtGui.QSlider()
		self.songTimeLabel = QtGui.QLabel()
		self.songTotalTimeLabel = QtGui.QLabel()
		self.songNameWidget = QtGui.QLabel()

		self.centerLayout = QtGui.QVBoxLayout()
		self.centerLayout.addWidget(self.bufferSlider,0,QtCore.Qt.AlignHCenter)
		self.centerLayout.addWidget(self.songNameWidget,0,QtCore.Qt.AlignHCenter)
		self.centerLayout.addStretch()

		#水平管理器
		self.title_layout = QtGui.QHBoxLayout()
		self.title_layout.addWidget(self.playPreBtn,0,QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
		self.title_layout.addWidget(self.playOrPauseBtn,0,QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
		self.title_layout.addWidget(self.playNextBtn,0,QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
		self.title_layout.addStretch()
		
		'''
		Constant	Value	Description
		Qt.AlignLeft	0x0001	Aligns with the left edge.
		Qt.AlignRight	0x0002	Aligns with the right edge.
		Qt.AlignHCenter	0x0004	Centers horizontally in the available space.
		Qt.AlignJustify	0x0008	Justifies the text in the available space.
		The vertical flags are:

		Constant	Value	Description
		Qt.AlignTop	0x0020	Aligns with the top.
		Qt.AlignBottom	0x0040	Aligns with the bottom.
		Qt.AlignVCenter	0x0080	Centers vertically in the available space.

		'''
		self.widget = QtGui.QWidget()
		self.setCentralWidget(self.widget)
		self.widget.setLayout(self.title_layout)

		self.setStyleSheet('''
		controlBar
		{
			border-image:url(bottom_bar_bg.tiff);
			border: 0px;
		}

		QPushButton#playPreBtn
		{
			min-width: 29px;
			max-width: 29px;
			min-height: 28px;
			max-width: 28px;
			border-image: url(previous_normal.tiff);
			qproperty-text: "";
		}
		QPushButton#playPreBtn:hover
		{
			border-image: url(previous_hover.tiff);
		}
		QPushButton#playPreBtn:pressed
		{
			border-image: url(previous_down.tiff);
		}

		QPushButton#playNextBtn
		{
			min-width: 29px;
			max-width: 29px;
			min-height: 28px;
			max-width: 28px;
			border-image: url(next_normal.tiff);
			qproperty-toolTip: "233333";
			qproperty-text: "";
		}
		QPushButton#playNextBtn:hover
		{
			border-image: url(next_hover.tiff);
		}
		QPushButton#playNextBtn:pressed
		{
			border-image: url(next_down.tiff);
		}
		
		/*播放与暂停*/
		QCheckBox#playOrPauseBtn::indicator 
		{
			width: 29px;
			height: 28px;
		}
		QCheckBox#playOrPauseBtn
		{
			min-width: 29px;
			max-width: 29px;
			min-height: 28px;
			max-width: 28px;
			qproperty-text: "";
		}
		/*播放*/
		QCheckBox#playOrPauseBtn::indicator:unchecked
		{
			image:url("play_normal.tiff");
		}
		QCheckBox#playOrPauseBtn::indicator:unchecked:hover,
		QCheckBox#playOrPauseBtn::indicator:unchecked:pressed
		{
			image:url("play_down.tiff");
		}
		/*暂停*/
		QCheckBox#playOrPauseBtn::indicator::checked
		{
			image:url("pause_normal.tiff");
		}
		QCheckBox#playOrPauseBtn::indicator::checked:hover,
		QCheckBox#playOrPauseBtn::indicator::checked:pressed
		{
			image:url("pause_down.tiff");
		}

					''')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	testWidget = ContentWidget()
	testWidget.show()
	#testWidget2 = titleBar()
	#testWidget2.show()
	app.exec_()