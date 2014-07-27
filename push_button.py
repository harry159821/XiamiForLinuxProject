#!/usr/bin/python  
#-*-coding:utf-8-*-
'''
* @文件名   push_button.h
* @版本信息 copyright  2012-2013 Sugon. All rights reserved.
* @功能描述
*           PushButton类包含最小化、最大化、关闭、主菜单等按钮的特效
* @作者     王亮<wangliang@sugon.com>
* @日期     2012-01-06
* @功能描述   主要设置按钮样式、特效
* @作者  王亮 <wangliang@sugon.com>
'''

from PyQt4.QtGui import *
from PyQt4.Qt import *

class PushButton(QPushButton):
	def __init__(self,parent = None):
		super(PushButton,self).__init__(parent)
		
		#枚举值
		self.status = 0 #self.NORMAL
		#self.pixmap = QPixmap()
		#self.btn_width = 40 #按钮宽度
		#self.btn_height = 20#按钮高度
		#self.mouse_press = False #按钮左键是否按下		

	def loadPixmap(self, pic_name):	
		self.pixmap = QPixmap(pic_name)
		self.btn_width = self.pixmap.width()/4
		self.btn_height = self.pixmap.height()
		self.setFixedSize(self.btn_width, self.btn_height)
		
	
	def enterEvent(self,event):	
		self.status = 1 #self.ENTER
		self.update()
	

	def mousePressEvent(self,event):	
		#若点击鼠标左键
		if(event.button() == Qt.LeftButton):		
			self.mouse_press = True
			self.status = 2 #self.PRESS
			self.update()		

	def mouseReleaseEvent(self,event):	
		#若点击鼠标左键
		if(self.mouse_press):		
			self.mouse_press = False
			self.status = 3 #self.ENTER
			self.update()
			self.clicked.emit(True)		

	def leaveEvent(self,event):	
		self.status = 0 #self.NORMAL
		self.update()
	

	def paintEvent(self,event):	
		self.painter = QPainter()
		self.painter.begin(self)
		self.painter.drawPixmap(self.rect(), self.pixmap.copy(self.btn_width * self.status, 0, self.btn_width, self.btn_height))
		self.painter.end()
		
if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	
	btn = PushButton()
	btn.loadPixmap("./img/sysButton/close.png")
	btn.show()
	
	sys.exit(app.exec_())
		
	
	

	
