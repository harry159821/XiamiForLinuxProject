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
		self.setWindowIconText('Xiami For Linux')
		self.setWindowTitle('Xiami For Linux')

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
						border: 1px;
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
		#self.main_splitter.setStyleSheet("QSplitter.handle{background:gray}")

		self.content_splitter = QtGui.QSplitter()
		self.content_splitter.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
		self.content_splitter.setOrientation(QtCore.Qt.Horizontal)
		self.content_splitter.setHandleWidth(1)
		self.content_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")

		self.TreeList = TreeWidget()

		self.titlebar = titleBar()
		self.titlebar.resize(1000, 50)
		self.titlebar.setMinimumSize(1000,50)
		self.titlebar.setMaximumHeight(50)

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
		#self.window_attribute()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		self.widget = ShadowWidget()
		self.setCentralWidget(self.widget)
		self.widget.setLayout(self.main_layout)
		#self.widget.setFixedSize(1000,650)

		#self.widget.setStyleSheet('''			
		#	border-style: solid; border-width: 5px;
		#	''')
	
		#双屏时居中会错误
		self.move(140,25)

		# 阴影测试Failed
		# shadow_effect = QtGui.QGraphicsDropShadowEffect(self)
		# shadow_effect.setOffset(-5, 5)
		# shadow_effect.setOffset(4.0)
		# shadow_effect.setColor(QtCore.Qt.gray)
		# shadow_effect.setColor(QtGui.QColor(0, 0, 0, 50))
		# shadow_effect.setBlurRadius(8)
		# self.setGraphicsEffect(shadow_effect)

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
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

	def paintEvent2(self,event):
		# 1.
		#p = QtGui.QPainter(self)
		#p.drawPixmap(0, 0, self.rect().width(), self.rect().height(), QtGui.QPixmap('main_shadow.png'))
		
		# 2.
		path = QtGui.QPainterPath()
		path.setFillRule(QtCore.Qt.WindingFill)
		path.addRect(10, 10, self.width()-20, self.height()-20)

		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing,True)
		painter.fillPath(path, QtGui.QBrush(QtCore.Qt.white))

		color = QtGui.QColor(0, 0, 0, 50)

		for i in range(1,10):
			path = QtGui.QPainterPath()
			path.setFillRule(QtCore.Qt.WindingFill)
			path.addRect(10-i, 10-i, self.width()-(10-i)*2, self.height()-(10-i)*2)
			color.setAlpha(150 - math.sqrt(i)*50)
			painter.setPen(color)
			painter.drawPath(path)

	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

class ShadowWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(ShadowWidget,self).__init__()
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

	def paintEvent(self,event):
		# 1.
		p = QtGui.QPainter(self)
		p.drawPixmap(0, 0, self.rect().width(), self.rect().height(), QtGui.QPixmap('main_shadow.png'))
		
		# 2.
		path = QtGui.QPainterPath()
		path.setFillRule(QtCore.Qt.WindingFill)
		path.addRect(10, 10, self.width()-20, self.height()-20)
		painter = QtGui.QPainter(self)
		painter.setRenderHint(QtGui.QPainter.Antialiasing,True)
		painter.fillPath(path, QtGui.QBrush(QtCore.Qt.white))
		color = QtGui.QColor(0, 0, 0, 50)
		for i in range(1,10):
			path = QtGui.QPainterPath()
			path.setFillRule(QtCore.Qt.WindingFill)
			path.addRect(10-i, 10-i, self.width()-(10-i)*2, self.height()-(10-i)*2)
			color.setAlpha(150 - math.sqrt(i)*50)
			painter.setPen(color)
			painter.drawPath(path)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

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
			border-top-left-radius:5px;
			border-top-right-radius:5px;
			border-bottom-right-radius:0px;
			border-bottom-left-radius:0px;
			border-style: solid;
			background: qlineargradient(spread:reflect,
			x1:1, y1:1, x2:1, y1:1,
			stop:1 rgba(230, 230, 230, 255),
			stop:0 rgba(175, 175, 175, 255));
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
		self.centerLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
		self.centerLayout.addWidget(self.emptyLabel  		,0,QtCore.Qt.AlignRight)
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
		self.widget.setLayout(self.control_layout)

		self.setStyleSheet('''
		controlBar
		{
			border-image:url(bottom_bar_bg.tiff);
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
			image: url("like_button_light_normal.tiff");
		}
		QCheckBox#favSongCheckBox::indicator:unchecked:hover
		{
			image: url("like_button_light_hover.tiff")
		}
		QCheckBox#favSongCheckBox::indicator:unchecked:pressed
		{
			image: url("like_button_light_normal.tiff");
		}
		QCheckBox#favSongCheckBox::indicator::checked
		{
			image: url("like_button_light_down.tiff");
		}
		QCheckBox#favSongCheckBox::indicator::checked:hover,
		QCheckBox#favSongCheckBox::indicator::checked:pressed
		{
			image: url("like_button_light_down.tiff");
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
			image: url("lyric_button_normal.tiff");
		}
		QCheckBox#deskLrcBtn::indicator:unchecked:hover
		{
			image: url("lyric_button_hover.tiff")
		}
		QCheckBox#deskLrcBtn::indicator:unchecked:pressed
		{
			image: url("lyric_button_hover.tiff");
		}
		QCheckBox#deskLrcBtn::indicator::checked
		{
			image: url("lyric_button_on.tiff");
		}
		QCheckBox#deskLrcBtn::indicator::checked:hover,
		QCheckBox#deskLrcBtn::indicator::checked:pressed
		{
			image: url("lyric_button_down.tiff");
		}

		/*相似歌曲*/
		QPushButton#similarSongsBtn
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 21px;
			max-height: 21px;
			spacing: 0px;
			border-image: url("smart_match_normal.tiff");
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
			border-image: url("smart_match_hover.tiff");
		}
		QPushButton#similarSongsBtn:pressed
		{
			border-image: url("smart_match_hover.tiff");
		}
		QPushButton#similarSongsBtn:disabled
		{
			border-image: url("smart_match_hover.tiff");
		}

		/*歌曲分享*/
		QPushButton#shareSongBtn
		{
			min-width: 21px;
			max-width: 21px;
			min-height: 21px;
			max-height: 21px;
			spacing: 0px;
			border-image: url("share_button_normal.tiff");
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
			border-image: url("share_button_hover.tiff");
		}
		QPushButton#shareSongBtn:pressed
		{
			border-image: url("share_button_on.tiff");
		}
		QPushButton#shareSongBtn:disabled
		{
			border-image: url("share_button_down.tiff");
		}

		/*音量*/
		QPushButton#volumeBtn
		{
			min-width: 20px;
			max-width: 20px;
			min-height:20px;
			max-width: 20px;
			image:url("volume_2_down.tiff");
		}
		QPushButton#volumeBtn:hover
		{
			image:url("volume_2_hover.tiff");
		}
		QPushButton#volumeBtn:pressed
		{
			image:url("volume_2_down.tiff");
		}

		/*播放模式*/
		QPushButton#playModeBtn
		{
			min-width:  20px;
			max-width:  20px;
			min-height: 20px;
			max-height: 20px;
			qproperty-text: "";
			image:url("fullscreen_repeat_all_normal.tiff");
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
			image: url("playlist_button_normal.tiff");
		}
		QCheckBox#playList::indicator:unchecked:hover
		{
			image: url("playlist_button_hover.tiff")
		}
		QCheckBox#playList::indicator:unchecked:pressed
		{
			image: url("playlist_button_hover.tiff");
		}
		QCheckBox#playList::indicator::checked
		{
			image: url("playlist_button_on.tiff");
		}
		QCheckBox#playList::indicator::checked:hover,
		QCheckBox#playList::indicator::checked:pressed
		{
			image: url("playlist_button_down.tiff");
		}

					''')

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	testWidget = ContentWidget()
	testWidget.show()
	#testWidget2 = titleBar()
	#testWidget2.show()
	app.exec_()