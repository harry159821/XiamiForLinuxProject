#!/usr/bin/python
# -*- coding:utf-8 -*-
import os,sys,math
from PyQt4 import QtGui,QtCore,Qt
'''
Xiami For Linux Project
'''
class ContentWidget(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(ContentWidget,self).__init__()
		self.setWindowIcon(QtGui.QIcon('default_user.ico'))
		self.setWindowTitle(u'Xiami For Linux')

		self.List = QtGui.QListWidget()
		self.List.setShortcutEnabled(True)
		item = ['1','2','3','4']
		listItem = []
		for i in item:
			listItem.append(QtGui.QListWidgetItem(i))
		for i in listItem:
			self.List.addItem(i)

		self.List.resize(500,560)
		#自适应窗口宽度
		self.List.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		#去除难看的边框
		self.List.setStyleSheet("""
						border-top: 	0px solid #adadad;
						border-left: 	0px solid #919191;
						border-right: 	1px solid #919191;
						border-bottom: 	0px solid #919191;
						""")

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

		self.content_splitter = QtGui.QSplitter()
		self.content_splitter.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
		self.content_splitter.setOrientation(QtCore.Qt.Horizontal)
		self.content_splitter.setHandleWidth(1)
		self.content_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")

		self.TreeList = TreeWidget()

		self.titlebar = titleBar(master=self)
		self.titlebar.resize(1000, 50)
		self.titlebar.setMinimumSize(1000,50)
		self.titlebar.setMaximumHeight(50)
		self.titlebar.title_label.setText(u'虾米音乐')

		self.ControlBar = controlBar()
		self.ControlBar.resize(1000, 60)
		self.ControlBar.setMinimumSize(1000,60)
		self.ControlBar.setMaximumHeight(60)

		self.TreeList.tree.resize(197,560)
		self.TreeList.tree.setMaximumWidth(197)
		self.TreeList.tree.setMinimumWidth(197)
		self.TreeList.tree.setMinimumHeight(560)

		self.content_splitter.addWidget(self.TreeList.tree)
		self.content_splitter.addWidget(self.List)
		self.content_splitter.setObjectName('content_splitter')

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
		self.main_layout.setContentsMargins(10,7,10,7)

		#窗口属性
		#self.window_attribute()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		self.widget = QtGui.QWidget()
		self.setCentralWidget(self.widget)
		self.widget.setLayout(self.main_layout)
		#self.widget.setFixedSize(1000,650)
		self.widget.setObjectName('main')
		self.setObjectName('main')

		#功能性功能开始
		self.titlebar.min_button.clicked.connect(self.hideIt)
		self.titlebar.max_button.clicked.connect(self.MaxAndNormal)
		self.titlebar.close_button.clicked.connect(self.closeIt)

		self.desktop = QtGui.QApplication.desktop()
		self.normalGeometry2 = self.geometry()
		self.animationEndFlag = 1
		print self.geometry(),self.widget.geometry(),self.normalGeometry()

		#双屏时居中会错误
		self.center()
		#self.move(140,25)

		#界面出现动画
		self.animation = QtCore.QPropertyAnimation(self,"windowOpacity")
		self.animation.setDuration(300)
		self.animation.setStartValue(0)
		self.animation.setEndValue(1)
		self.animation.start()
		#功能性功能结束

	def closeIt(self):
		self.animation = QtCore.QPropertyAnimation(self,"windowOpacity")
		self.animation.finished.connect(QtCore.QCoreApplication.instance().quit)
		self.animation.setDuration(300)
		self.animation.setStartValue(1)
		self.animation.setEndValue(0)
		self.animation.start()

	def hideIt(self):
		self.animation = QtCore.QPropertyAnimation(self,"windowOpacity")
		#self.animation.finished.connect(self.showMinimized)
		self.animation.setDuration(300)
		self.animation.setStartValue(1)
		self.animation.setEndValue(0)
		self.animation.start()

	def window_attribute(self):
		if os.name == 'nt':
			#隐藏窗口边框、背景、任务栏
			#self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.X11BypassWindowManagerHint | QtCore.Qt.SplashScreen)
			self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.X11BypassWindowManagerHint | QtCore.Qt.SplashScreen)
		else:
			self.setWindowFlags(QtCore.Qt.FramelessWindowHint )# | QtCore.Qt.Tool)
			#self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)# | QtCore.Qt.Tool)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
		self.setMouseTracking(True)
		#窗口透明度
		#self.setWindowOpacity(0.9)

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QtGui.QApplication.postEvent(self, QtCore.QEvent(174))
			event.accept()

	def mouseMoveEvent(self, event):
		if self.isFullScreen():
			self.main_layout.setContentsMargins(10,7,10,7)
			self.animation = QtCore.QPropertyAnimation(self,"geometry")
			self.animation.setDuration(160)
			self.animation.setEndValue(self.normalGeometry2)
			self.animation.setStartValue(self.desktop.availableGeometry(self.desktop.screenNumber(self.widget)))
			self.animation.finished.connect(self.showNormal2)
			self.animationEndFlag = 0
			self.animation.start()
			event.accept()
		else:
			#缩放动画停止前不允许窗口拖动
			if self.animationEndFlag:
				self.normalGeometry2 = self.geometry()
				if event.buttons() == QtCore.Qt.LeftButton:
					self.move(event.globalPos() - self.dragPosition)
					event.accept()

	def MaxAndNormal(self):
		'''最大化与正常大小间切换'''
		if self.showNormal3():
			self.showFullScreen3()

	def showNormal2(self):
		self.animationEndFlag = 1#动画停止
		self.showNormal()

	def showNormal3(self):
		if self.isFullScreen():
			self.main_layout.setContentsMargins(10,7,10,7)
			self.animation = QtCore.QPropertyAnimation(self,"geometry")
			self.animation.setDuration(180)
			self.animation.setEndValue(self.normalGeometry2)
			self.animation.setStartValue(self.desktop.availableGeometry(self.desktop.screenNumber(self.widget)))
			self.animation.finished.connect(self.showNormal2)
			self.animationEndFlag = 0
			self.animation.start()
			return 0
		return 1

	def showFullScreen2(self):
		self.animationEndFlag = 1#动画停止
		self.showFullScreen()

	def showFullScreen3(self):
		if not self.isFullScreen():
			self.main_layout.setContentsMargins(0,0,0,0)
			self.animation = QtCore.QPropertyAnimation(self,"geometry")
			self.animation.setDuration(180)
			self.animation.setStartValue(self.geometry())
			self.animation.setEndValue(self.desktop.availableGeometry(self.desktop.screenNumber(self.widget)))
			self.animation.finished.connect(self.showFullScreen2)
			self.animationEndFlag = 0
			self.animation.start()

	def paintEvent(self,event):
		# 窗口阴影
		p = QtGui.QPainter(self)
		p.drawPixmap(0, 0, self.rect().width(), self.rect().height(), QtGui.QPixmap('img/mainwindow/main_shadow2.png'))

	def center(self):
		#screen = QtGui.QDesktopWidget().screenGeometry()
		#screen = self.desktop.availableGeometry(self.desktop.screenNumber(self.widget))
		screen = self.desktop.availableGeometry(1)
		size = self.geometry()
		print 'screen:',screen
		print 'size:',size
		print 'rect:',self.rect()
		print 'widget rect:',self.widget.rect()
		print 'pos:',self.pos()
		print 'widget pos:',self.widget.pos()
		print 'frameSize:',self.frameSize()
		print 'widget frameSize:',self.widget.frameSize()
		print 'move:',(screen.width()-size.width())/2, (screen.height()-size.height())/2

		self.move(0,0)
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

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
		#去除虚线
		self.tree.setFocusPolicy(QtCore.Qt.NoFocus)

		root = QtGui.QTreeWidgetItem(self.tree)
		root.setText(0,u'  发现')

		self.tree.expandItem(root)

		self.setStyleSheet("""
						border: 0px;
						""")

		# 相对路径统一成path/path/path.path格式
		# margin :外边距
		# padding:内边距
		self.tree.setStyleSheet("""

		QTreeView
		{
			selection-background-color: transparent;
			show-decoration-selected: 1;
			background:url('img/gray2.png');
			margin : -2px 2px 0px -4px;
			border-top: 	2px solid #919191;
			border-left: 	5px solid #919191;
			border-right: 	0px solid red;
			border-bottom: 	0px solid red;
		}

		QTreeWidget::item
		{
			height:32px;
		  /*margin: top right bottom left*/
			margin : 0px 4px 0px -4px;
			padding: 0px 0px 0px 20px;
		}

		QTreeView::item:has-children
		{
			margin : 0px 4px 0px 8px;
			padding: 0px 0px 0px 0px;
		}

		QTreeView::item:has-children:hover
		{
			margin : 0px 4px 0px 4px;
			padding: 0px 0px 0px -4px;
		}

		QTreeView::item:has-children:selected
		{
			color:lightgray;
			margin : 0px 4px 0px 8px;
			padding: 0px 0px 0px -8px;
		}

		QTreeView::item:hover
		{
			margin : 0px 4px 0px -4px;
			padding: 0px 0px 0px 8px;
			background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
			/*border-image:url(img/bottom_bar_bg.tiff);*/
			/*border: 1px solid #bfcde4;*/
		}

		QTreeView::item:selected
		{
			color:lightgray;
			margin : 0px 4px 0px -4px;
			padding: 0px 0px 0px 8px;			
			background-color:rgb(30,39,45,255);
			/*border: 1px solid #567dbc;*/
		}

						""")

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
		root2.setText(0,u'  我的音乐')
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

		#self.setCentralWidget(self.tree)
		#self.resize(200,450)

class titleBar(QtGui.QMainWindow):

	def __init__(self,master,parent=None):
		super(titleBar,self).__init__()
		self.master = master

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

		self.close_button.setIcon(QtGui.QIcon("img/orange.png"))
		self.min_button.setIcon(QtGui.QIcon("img/green.png"))
		self.max_button.setIcon(QtGui.QIcon("img/blue.png"))		

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

		#给窗口处理
		#self.close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)

		pixmap = QtGui.QPixmap('')
		icon   = QtGui.QIcon('')
		size   = QtCore.QSize(pixmap.size().width() + 6, pixmap.size().height() + 4)

		self.searchbtn = QtGui.QPushButton(icon, "")
		#self.searchbtn.setMinimumSize(size)
		#self.searchbtn.setMaximumSize(size)
		#self.searchbtn.setFocusPolicy(QtCore.Qt.NoFocus)
		self.searchbtn.setFlat(True)
		self.searchbtn.setDefault(True)

		self.searchLine = QtGui.QLineEdit()
		# self.searchLine.setStyleSheet("""
		# 							border:2px groove gray;
		# 							border-radius:10px;
		# 							text-align:center;
		# 							padding:2px 10px;
		# 							background:white;
		# 							""")

		buttonLayout = QtGui.QHBoxLayout()
		#buttonLayout.setContentsMargins(0, 0, 0, 0)
		#buttonLayout.addStretch()
		buttonLayout.addWidget(self.searchbtn)
		self.searchLine.setLayout(buttonLayout)
		#self.searchLine.setTextMargins(0, 1, pixmap.size().width(), 1)

		'''
		border-radius可以同时设置1到4个值。
		如果设置1个值，表示4个圆角都使用这个值。
		如果设置两个值，表示左上角和右下角使用第一个值，右上角和左下角使用第二个值。
		如果设置三个值，表示左上角使用第一个值，右上角和左下角使用第二个值，右下角使用第三个值。
		如果设置四个值，则依次对应左上角、右上角、右下角、左下角（顺时针顺序）。
		'''
		self.setStyleSheet('''
		.QMainWindow
		{
			background:transparent;
			border-bottom:10px;
		}
		.QWidget
		{
			border-top-left-radius:		8px;
			border-top-right-radius:	8px;
			border-bottom-right-radius:	0px;
			border-bottom-left-radius:	0px;
			border-style: solid;
			background: qlineargradient(spread:reflect,
			x1:1, y1:1, x2:1, y1:1,
			stop:1 rgba(230, 230, 230, 255),
			stop:0 rgba(175, 175, 175, 255));

			border-top: 	1px solid #919191;
			border-left: 	1px solid #919191;
			border-right: 	1px solid #919191;
			border-bottom: 	2px solid #adadad;
		}
		/*搜索*/
		QLineEdit
		{
			height: 21px;
			min-width: 120px;   
			max-width: 120px;
			min-height: 21px;
			max-height: 21px;
			padding: -5px;
			border: 5px;
			border-image: url("img/nav_srch_input.png") 5;
		}
		QLineEdit QPushButton#searchbtn
		{
			max-width: 15px;
			max-height: 15px;
			border-image: url("img/nav_srch_btn_click.png");
			qproperty-toolTip: "搜索";
		}
		QLineEdit QPushButton#searchbtn:hover
		{
			border-image: url("img/nav_srch_btn_click.png");
		}
		QLineEdit QPushButton#searchbtn:pressed
		{
			border-image: url("img/nav_srch_btn.png");
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

	def wheelEvent(self,event):
		if self.master.animationEndFlag and event.delta()>0:
			self.master.showFullScreen3()
		if self.master.animationEndFlag and event.delta()<0:
			self.master.showNormal3()

	def mouseDoubleClickEvent(self,event):
		'''双击标题栏'''
		self.master.MaxAndNormal()

class controlBar(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(controlBar,self).__init__(parent)
		self.setAutoFillBackground(True)

		#palette = QtGui.QPalette()
		#palette.setBrush(QtGui.QPalette.Background,
		#	QtGui.QBrush(QtGui.QPixmap("img/bottom_bar_bg.tiff")))
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

		#进度条
		self.bufferSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
		self.bufferSlider.setObjectName('bufferSlider')
		self.bufferSlider.setMinimumWidth(290)
		#已播放时间
		self.songTimeLabel = QtGui.QLabel()
		self.songTimeLabel.setObjectName('songTimeLabel')
		#歌曲总时间
		self.songTotalTimeLabel = QtGui.QLabel()
		self.songTotalTimeLabel.setObjectName('songTotalTimeLabel')
		#歌曲名称
		self.songNameWidget = QtGui.QLabel()
		self.songNameWidget.setObjectName('songNameWidget')
		#播放模式
		self.playModeBtn = QtGui.QPushButton()
		self.playModeBtn.setObjectName('playModeBtn')
		#声音调节
		self.volumeBtn = QtGui.QPushButton()
		self.volumeBtn.setObjectName('volumeBtn')
		#歌曲收藏否
		self.favSongCheckBox = QtGui.QCheckBox()
		self.favSongCheckBox.setObjectName('favSongCheckBox')
		#桌面歌词
		self.deskLrcBtn = QtGui.QCheckBox()
		self.deskLrcBtn.setObjectName('deskLrcBtn')
		#相似歌曲
		self.similarSongsBtn = QtGui.QPushButton()
		self.similarSongsBtn.setObjectName('similarSongsBtn')
		#歌曲分享
		self.shareSongBtn = QtGui.QPushButton()
		self.shareSongBtn.setObjectName('shareSongBtn')
		#播放列表按钮
		self.playList = QtGui.QCheckBox()
		self.playList.setObjectName('playList')
		#间隔Label
		self.emptyLabel = QtGui.QLabel()
		self.emptyLabel.setObjectName('emptyLabel')

		self.midLayout = QtGui.QVBoxLayout()
		self.midLayout.addWidget(self.bufferSlider,  0,QtCore.Qt.AlignHCenter)
		self.midLayout.addWidget(self.songNameWidget,0,QtCore.Qt.AlignHCenter)

		self.leftLayout   = QtGui.QHBoxLayout()
		self.centerLayout = QtGui.QHBoxLayout()
		self.rightLayout  = QtGui.QHBoxLayout()

		#self.leftLayout.setSpacing(5)
		self.leftLayout.addWidget(self.playPreBtn, 	 	0,QtCore.Qt.AlignLeft)
		self.leftLayout.addWidget(self.playOrPauseBtn, 	0,QtCore.Qt.AlignLeft)
		self.leftLayout.addWidget(self.playNextBtn, 	0,QtCore.Qt.AlignLeft)
		self.leftLayout.setAlignment(self.playOrPauseBtn,QtCore.Qt.AlignLeft)
		
		#self.centerLayout.setSpacing(5)
		#self.centerLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
		#self.centerLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
		self.centerLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
		self.centerLayout.addWidget(self.playModeBtn 		,0,QtCore.Qt.AlignHCenter)
		self.centerLayout.addWidget(self.songTimeLabel 		,0,QtCore.Qt.AlignHCenter)
		self.centerLayout.addLayout(self.midLayout 			,0)
		self.centerLayout.addWidget(self.songTotalTimeLabel ,0,QtCore.Qt.AlignHCenter)
		self.centerLayout.addWidget(self.volumeBtn 			,0,QtCore.Qt.AlignHCenter)
		
		#self.rightLayout.setSpacing(1)
		self.rightLayout.addWidget(self.favSongCheckBox 	,0,QtCore.Qt.AlignRight)
		self.rightLayout.addWidget(self.deskLrcBtn 			,0,QtCore.Qt.AlignRight)
		self.rightLayout.addWidget(self.similarSongsBtn 	,0,QtCore.Qt.AlignRight)
		self.rightLayout.addWidget(self.shareSongBtn 		,0,QtCore.Qt.AlignRight)
		self.rightLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
		self.rightLayout.addWidget(self.playList 			,0,QtCore.Qt.AlignRight)

		#水平管理器
		self.control_layout = QtGui.QHBoxLayout()
		self.control_layout.addLayout(self.leftLayout   ,0)
		self.control_layout.addStretch()
		self.control_layout.addLayout(self.centerLayout ,0)
		self.control_layout.addStretch()
		self.control_layout.addLayout(self.rightLayout  ,0)
		self.control_layout.setSpacing(10)
		#setContentMargins(10, 10, 10, 10)
		
		self.bufferSlider.setMinimum(0)
		self.bufferSlider.setMaximum(100)
		self.bufferSlider.setValue(50)
		self.songTimeLabel.setText('01:23')
		self.songTotalTimeLabel.setText('03:23')
		self.songNameWidget.setText('icarus')
		self.emptyLabel.setText('   ')

		self.font = QtGui.QFont()
		self.font.setPixelSize(11)   #设置字号32,以像素为单位
		self.font.setFamily("SimSun")#设置字体，宋体
		self.font.setFamily(u"微软雅黑")
		#self.font.setWeight(20)     #设置字型,不加粗
		self.font.setBold(True)
		self.font.setItalic(False)   #设置字型,不倾斜
		self.font.setUnderline(False)#设置字型,无下划线

		self.songTimeLabel.setFont(self.font)
		self.songTotalTimeLabel.setFont(self.font)
		self.songNameWidget.setFont(self.font)
		'''
		Constant	    Value	Description
		Qt.AlignLeft	0x0001	Aligns with the left edge.
		Qt.AlignRight	0x0002	Aligns with the right edge.
		Qt.AlignHCenter	0x0004	Centers horizontally in the available space.
		Qt.AlignJustify	0x0008	Justifies the text in the available space.
		The vertical flags are:

		Constant	    Value	Description
		Qt.AlignTop	    0x0020	Aligns with the top.
		Qt.AlignBottom	0x0040	Aligns with the bottom.
		Qt.AlignVCenter	0x0080	Centers vertically in the available space.

		'''
		self.widget = QtGui.QWidget()
		self.setCentralWidget(self.widget)
		self.widget.setLayout(self.control_layout)

		self.setStyleSheet('''
		controlBar
		{
			border-image:url(img/bottom_bar_bg.tiff);
			border: 0px;
		}
		/*貌似因为背景图片圆角没起作用*/
		.QMainWindow
		{
			background:transparent;
		}
		controlBar QWidget
		{
			border-top-left-radius:0px;
			border-top-right-radius:0px;
			border-bottom-right-radius:5px;
			border-bottom-left-radius:5px;
		}

		QPushButton#playPreBtn
		{
			min-width: 29px;
			max-width: 29px;
			min-height: 28px;
			max-width: 28px;
			border-image: url(img/control/previous_normal.tiff);
			qproperty-text: "";
		}
		QPushButton#playPreBtn:hover
		{
			border-image: url(img/control/previous_hover.tiff);
		}
		QPushButton#playPreBtn:pressed
		{
			border-image: url(img/control/previous_down.tiff);
		}

		QPushButton#playNextBtn
		{
			min-width: 29px;
			max-width: 29px;
			min-height: 28px;
			max-width: 28px;
			border-image: url(img/control/next_normal.tiff);
			qproperty-toolTip: "233333";
			qproperty-text: "";
		}
		QPushButton#playNextBtn:hover
		{
			border-image: url(img/control/next_hover.tiff);
		}
		QPushButton#playNextBtn:pressed
		{
			border-image: url(img/control/next_down.tiff);
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
			image:url("img/control/play_normal.tiff");
		}
		QCheckBox#playOrPauseBtn::indicator:unchecked:hover,
		QCheckBox#playOrPauseBtn::indicator:unchecked:pressed
		{
			image:url("img/control/play_down.tiff");
		}
		/*暂停*/
		QCheckBox#playOrPauseBtn::indicator::checked
		{
			image:url("img/control/pause_normal.tiff");
		}
		QCheckBox#playOrPauseBtn::indicator::checked:hover,
		QCheckBox#playOrPauseBtn::indicator::checked:pressed
		{
			image:url("img/control/pause_down.tiff");
		}
		/*歌曲名*/
		QLabel#songNameWidget
		{
			color:gray;
		}
		QLabel#songTotalTimeLabel
		{
			color:gray;
		}
		QLabel#songTimeLabel
		{
			color:gray;
		}
		/*收藏*/
		QCheckBox#favSongCheckBox
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 26px;
			max-height: 26px;
			spacing: 0px;
			qproperty-toolTip: "收藏";
			qproperty-text: "";
		}
		QCheckBox#favSongCheckBox::indicator 
		{
			width: 21px;
			height: 26px;
		}
		QCheckBox#favSongCheckBox::indicator:unchecked
		{
			image: url("img/control/like_button_light_normal.tiff");
		}
		QCheckBox#favSongCheckBox::indicator:unchecked:hover
		{
			image: url("img/control/like_button_light_hover.tiff")
		}
		QCheckBox#favSongCheckBox::indicator:unchecked:pressed
		{
			image: url("img/control/like_button_light_normal.tiff");
		}
		QCheckBox#favSongCheckBox::indicator::checked
		{
			image: url("img/control/like_button_light_down.tiff");
		}
		QCheckBox#favSongCheckBox::indicator::checked:hover,
		QCheckBox#favSongCheckBox::indicator::checked:pressed
		{
			image: url("img/control/like_button_light_down.tiff");
		}

		/*桌面歌词*/
		QCheckBox#deskLrcBtn
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 26px;
			max-height: 26px;
			spacing: 0px;
			qproperty-toolTip: "歌词";
			qproperty-text: "";
		}
		QCheckBox#deskLrcBtn::indicator 
		{
			width: 21px;
			height: 26px;
		}
		QCheckBox#deskLrcBtn::indicator:unchecked
		{
			image: url("img/control/lyric_button_normal.tiff");
		}
		QCheckBox#deskLrcBtn::indicator:unchecked:hover
		{
			image: url("img/control/lyric_button_hover.tiff")
		}
		QCheckBox#deskLrcBtn::indicator:unchecked:pressed
		{
			image: url("img/control/lyric_button_hover.tiff");
		}
		QCheckBox#deskLrcBtn::indicator::checked
		{
			image: url("img/control/lyric_button_on.tiff");
		}
		QCheckBox#deskLrcBtn::indicator::checked:hover,
		QCheckBox#deskLrcBtn::indicator::checked:pressed
		{
			image: url("img/control/lyric_button_down.tiff");
		}

		/*相似歌曲*/
		QPushButton#similarSongsBtn
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 21px;
			max-height: 21px;
			spacing: 0px;
			border-image: url("img/control/smart_match_normal.tiff");
			qproperty-toolTip: "相似歌曲";
			qproperty-text: "";
		}
		QPushButton#similarSongsBtn::indicator 
		{
			width: 21px;
			height: 21px;
		}
		QPushButton#similarSongsBtn:hover
		{
			border-image: url("img/control/smart_match_hover.tiff");
		}
		QPushButton#similarSongsBtn:pressed
		{
			border-image: url("img/control/smart_match_hover.tiff");
		}
		QPushButton#similarSongsBtn:disabled
		{
			border-image: url("img/control/smart_match_hover.tiff");
		}

		/*歌曲分享*/
		QPushButton#shareSongBtn
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 21px;
			max-height: 21px;
			spacing: 0px;
			border-image: url("img/control/share_button_normal.tiff");
			qproperty-toolTip: "歌曲分享";
			qproperty-text: "";
		}
		QPushButton#shareSongBtn::indicator 
		{
			width: 21px;
			height: 21px;
		}
		QPushButton#shareSongBtn:hover
		{
			border-image: url("img/control/share_button_hover.tiff");
		}
		QPushButton#shareSongBtn:pressed
		{
			border-image: url("img/control/share_button_on.tiff");
		}
		QPushButton#shareSongBtn:disabled
		{
			border-image: url("img/control/share_button_down.tiff");
		}

		/*音量*/
		QPushButton#volumeBtn
		{
			min-width: 20px;
			max-width: 20px;
			min-height:20px;
			max-width: 20px;
			image:url("img/control/volume_2_down.tiff");
		}
		QPushButton#volumeBtn:hover
		{
			image:url("img/control/volume_2_hover.tiff");
		}
		QPushButton#volumeBtn:pressed
		{
			image:url("img/control/volume_2_down.tiff");
		}

		/*播放模式*/
		QPushButton#playModeBtn
		{
			min-width:  20px;
			max-width:  20px;
			min-height: 20px;
			max-height: 20px;
			qproperty-text: "";
			image:url("img/control/fullscreen_repeat_all_normal.tiff");
		}

		/*进度条*/
		QSlider::groove:horizontal
		{
			border:0px;
			height:4px;
		}  
		QSlider::sub-page:horizontal
		{
			background:orange;
		}  
		QSlider::add-page:horizontal
		{
			background:gray;
		} 
		QSlider::handle:horizontal
		{
			background:white;
			width:10px;
			border-radius:5px;
			margin:-3px 0px -3px 0px;
		}

		/*播放列表按钮*/
		QCheckBox#playList
		{
			min-width: 23px;
			max-width: 23px;
			min-height: 23px;
			max-height: 23px;
			spacing: 0px;
			qproperty-toolTip: "播放列表";
			qproperty-text: "";
		}
		QCheckBox#playList::indicator 
		{
			width: 23px;
			height: 23px;
		}
		QCheckBox#playList::indicator:unchecked
		{
			image: url("img/control/playlist_button_normal.tiff");
		}
		QCheckBox#playList::indicator:unchecked:hover
		{
			image: url("img/control/playlist_button_hover.tiff")
		}
		QCheckBox#playList::indicator:unchecked:pressed
		{
			image: url("img/control/playlist_button_hover.tiff");
		}
		QCheckBox#playList::indicator::checked
		{
			image: url("img/control/playlist_button_on.tiff");
		}
		QCheckBox#playList::indicator::checked:hover,
		QCheckBox#playList::indicator::checked:pressed
		{
			image: url("img/control/playlist_button_down.tiff");
		}

					''')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	testWidget = ContentWidget()
	testWidget.show()
	sys.exit(app.exec_())