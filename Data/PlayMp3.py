# -*- coding:utf-8 -*-

import sys
try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtMultimedia import *
except Exception, e:
    print e


class Player(QWidget):
    def __init__(self):
        super(Player, self).__init__()
        self.url = QUrl("http://m5.file.xiami.com/590/1288631590/397531/1769715717_15607117_l.mp3?auth_key=465e63951e7d97f2d74976fe03f88ea0-1441497600-0-null")
        self.url = QUrl("Lilac.mp3")
        # self.url = QUrl("http://localhost:8080/static/daoxiang.mp3")
        # self.url = QUrl("http://m5.file.xiami.com/565/75565/404080/1769787704_15590915_l.mp3?auth_key=23716ddf0073f7a5f28e98705b3ca10c-1442992279-0-null")
        self.content = QMediaContent(self.url)
        self.player = QMediaPlayer()
        self.player.setMedia(self.content)

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setGeometry(QRect(10, 90, 300, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        # self.horizontalSlider.setSliderPosition(80)
        self.horizontalSlider.valueChanged.connect(self.sliderPositionChanged)
        self.horizontalSlider.sliderPressed.connect(self.sliderPressed)
        self.horizontalSlider.sliderReleased.connect(self.sliderReleased)
        self.horizontalSlider.isPressed = False

        self.show()

        self.player.positionChanged.connect(self.positionChangeFun)
        self.player.play()

    def sliderPressed(self):
        print "sliderPressed"
        self.horizontalSlider.isPressed = True
        pass

    def sliderReleased(self):
        print "sliderReleased"
        self.player.setPosition(self.player.duration()*self.horizontalSlider.value()/100.0)
        self.horizontalSlider.isPressed = False
        pass

    def sliderPositionChanged(self,pos):
        print "sliderPositionChanged ",pos,self.player.duration()*pos/100.0
        # self.player.setPosition(self.player.duration()*pos/100.0)

    def positionChangeFun(self,pos):
        index = float(pos)/self.player.duration()*100
        print pos,self.player.duration(),index,type(index)
        if not self.horizontalSlider.isPressed:
            self.horizontalSlider.setSliderPosition(index+1)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = Player()
    # url = QUrl("http://m5.file.xiami.com/590/1288631590/397531/1769715717_15607117_l.mp3?auth_key=465e63951e7d97f2d74976fe03f88ea0-1441497600-0-null")
    # url = QUrl("Lilac.mp3")
    # url = QUrl("http://localhost:8080/static/daoxiang.mp3")
    # content = QMediaContent(url)
    # player = QMediaPlayer()    
    # player.setMedia(content)
    # player.setPosition(120000)
    # player.play()
    # sys.exit(1)
    sys.exit(app.exec_())