#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore,Qt

class guessYouLike(QtGui.QWidget):
    def __init__(self,parent=None):
        super(guessYouLike,self).__init__()

        self.playOrPauseBtn = QtGui.QCheckBox()
        self.playOrPauseBtn.setParent(self)
        self.playOrPauseBtn.setObjectName('playOrPauseBtn')
        self.playOrPauseBtn.move(self.size().width()/2,self.size().height()/2)

        self.setStyleSheet('''
        /*播放与暂停*/
        QCheckBox#playOrPauseBtn::indicator 
        {
            width: 50px;
            height: 50px;
        }
        QCheckBox#playOrPauseBtn
        {
            min-width: 50px;
            max-width: 50px;
            min-height: 50px;
            max-width: 50px;
            qproperty-text: "";
        }
        /*播放*/
        QCheckBox#playOrPauseBtn::indicator:unchecked
        {
            image:url("img/guessYouLike/guess_you_like_play_normal.tiff");
        }
        QCheckBox#playOrPauseBtn::indicator:unchecked:hover
        {
            image:url("img/guessYouLike/guess_you_like_play_hover.tiff");
        }
        QCheckBox#playOrPauseBtn::indicator:unchecked:pressed
        {
            image:url("img/guessYouLike/guess_you_like_play_down.tiff");
        }
        /*暂停*/
        QCheckBox#playOrPauseBtn::indicator::checked
        {
            image:url("img/guessYouLike/guess_you_like_pause_normal.tiff");
        }
        QCheckBox#playOrPauseBtn::indicator::checked:hover
        {
            image:url("img/guessYouLike/guess_you_like_pause_hover.tiff");
        }
        QCheckBox#playOrPauseBtn::indicator::checked:pressed
        {
            image:url("img/guessYouLike/guess_you_like_pause_down.tiff");
        }
        ''')

    def enterEvent(self,event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        
    def resizeEvent(self,event):
        self.playOrPauseBtn.move(self.size().width()/2,self.size().height()/2)

    def paintEvent(self,event):
        # 窗口阴影
        p = QtGui.QPainter(self)
        p.drawPixmap(0, 0, self.rect().width(), self.rect().height(), QtGui.QPixmap('img/guessYouLike/guess_you_like_bg.png'))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = guessYouLike()
    w.show()
    sys.exit(app.exec_())