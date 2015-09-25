# -*- coding:utf-8 -*-
import sys,time
import urllib

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import Phonon

class Player(QWidget):
    def __init__(self):
        super(Player, self).__init__()
        self.url = QUrl("http://m5.file.xiami.com/590/1288631590/397531/1769715717_15607117_l.mp3?auth_key=465e63951e7d97f2d74976fe03f88ea0-1441497600-0-null")
        self.url = QUrl("Lilac.mp3")
        self.url = QUrl("http://localhost:8080/static/daoxiang.mp3")
        self.url = QUrl("http://m5.file.xiami.com/565/75565/404080/1769787704_15590915_l.mp3?auth_key=23716ddf0073f7a5f28e98705b3ca10c-1442992279-0-null")

        url = "http://m5.file.xiami.com/565/75565/404080/1769787704_15590915_l.mp3?auth_key=23716ddf0073f7a5f28e98705b3ca10c-1442992279-0-null"

        self.mediaObject = Phonon.MediaObject(self)
        self.media = Phonon.MediaSource("nuo.mp3")
        self.mediaObject.setCurrentSource(self.media)

        # self.musicFile = QFile("nuo.mp3")
        # self.musicFile.open(QIODevice.ReadOnly)
        # self.someBuffer = QBuffer(self.musicFile.readAll())
        # self.someBuffer.open(QIODevice.ReadOnly)
        # someBuffer.writeData(urllib.urlopen(url).read(60000))
        # self.someBuffer.writeData(open("nuo.mp3",'r').read())

        # self.sourceWrapper = Phonon.MediaSource(self.someBuffer)
        # self.mediaObject.setCurrentSource(self.sourceWrapper)

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)

        Phonon.createPath(self.mediaObject, self.audioOutput)
        
        self.mediaObject.setTickInterval(100)
        self.mediaObject.tick.connect(self.tick)

        self.metaInformationResolver = Phonon.MediaObject(self)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
            
        self.button = QPushButton(self)
        self.button.clicked.connect(self.mediaObject.play)

        self.button2 = QPushButton(self)
        self.button2.clicked.connect(self.mediaObject.stop)
        self.button2.move(50,50)

        self.seekSlider = Phonon.SeekSlider(self)
        self.seekSlider.setMediaObject(self.mediaObject)
        self.seekSlider.move(10,30)

        self.metaInformationResolver.setCurrentSource(self.media)

        # self.mediaObject.stop()
        # self.mediaObject.clearQueue()
        # self.mediaObject.play()

        self.show()

    def metaStateChanged(self, newState, oldState):
        pass

    def tick(self, time):
        print time
        # displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        # print displayTime

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