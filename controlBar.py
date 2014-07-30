#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt

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
			border-image:url(img/bottom_bar_bg.tiff);
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

					''')

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	ControlBar = controlBar()
	ControlBar.show()
	sys.exit(app.exec_())	