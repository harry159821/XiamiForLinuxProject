#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)
        self.mediaObject.setTickInterval(100)
        self.mediaObject.tick.connect(self.tick)

        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.media = Phonon.MediaSource("nuo.mp3")
        self.metaInformationResolver.setCurrentSource(self.media)
        self.mediaObject.setCurrentSource(self.media)
        self.mediaObject.play()
        # self.player = Phonon.createPlayer(Phonon.MusicCategory,Phonon.MediaSource("nuo.mp3"))
        # self.player.play()

    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        print time

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Music Player")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
