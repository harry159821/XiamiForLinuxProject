from PyQt4 import QtGui,QtCore
import random
import sys

from PyQt4 import QtCore

class Thread(QtCore.QThread):    
    def __init__(self,parent=None):
        super(Thread, self).__init__()

        self.mutex = QtCore.QMutex()
        self.condition = QtCore.QWaitCondition()
        self.centerX = 0.0
        self.centerY = 0.0
        self.restart = False
                        
    def __del__(self):
        self.mutex.lock()
        self.abort = True
        self.condition.wakeOne()
        self.mutex.unlock()

        self.wait()

    def render(self, centerX, centerY):
        locker = QtCore.QMutexLocker(self.mutex)

        self.centerX = centerX
        self.centerY = centerY

        if not self.isRunning():
            self.start(QtCore.QThread.LowPriority)
        else:
            self.restart = True
            self.condition.wakeOne()        

    def run(self):
        while True:
            self.mutex.lock()
            centerX = self.centerX
            centerY = self.centerY
            self.mutex.unlock()            

            while centerX < centerY:
                for y in range(-halfHeight, halfHeight):
                    if self.restart:
                        break
                    if self.abort:
                        return   

            self.mutex.lock()
            if not self.restart:
                self.condition.wait(self.mutex)
            self.restart = False
            self.mutex.unlock()

class MandelbrotWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MandelbrotWidget, self).__init__(parent)

        self.thread = RenderThread()
        self.thread.renderedImage.connect(self.updatePixmap)

    def render(self):
        self.thread.render(self.centerX, self.centerY)        



# D:\Python27\Lib\site-packages\PyQt4\examples\threads\waitconditions.py
# Waitconditions
DataSize = 100000
BufferSize = 8192
buffer = list(range(BufferSize))

bufferNotEmpty = QtCore.QWaitCondition()
bufferNotFull = QtCore.QWaitCondition()
mutex = QtCore.QMutex()
numUsedBytes = 0


class Producer(QtCore.QThread):
    def run(self):
        global numUsedBytes

        for i in range(DataSize):
            mutex.lock()
            if numUsedBytes == BufferSize:
                bufferNotFull.wait(mutex)
            mutex.unlock()
            
            buffer[i % BufferSize] = "ACGT"[random.randint(0, 3)]

            mutex.lock()
            numUsedBytes += 1
            bufferNotEmpty.wakeAll()
            mutex.unlock()


class Consumer(QtCore.QThread):
    def run(self):
        global numUsedBytes

        for i in range(DataSize):
            mutex.lock()
            if numUsedBytes == 0:
                bufferNotEmpty.wait(mutex)
            mutex.unlock()
            
            sys.stderr.write(buffer[i % BufferSize])

            mutex.lock()
            numUsedBytes -= 1
            bufferNotFull.wakeAll()
            mutex.unlock()
            
        sys.stderr.write("\n")


if __name__ == '__main__':
    app = QtCore.QCoreApplication(sys.argv)
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.wait()
    consumer.wait()