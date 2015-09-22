from PyQt4 import QtGui,QtCore
import sys
from PIL import Image


class Windows(QtGui.QWidget):
    def __init__(self):
        super(Windows, self).__init__()
        self.resize(500,600)
        self.label = QtGui.QLabel(self)

        image = Image.open("harry159821@126.com.png")
        image.save("harry159821@126.com.png","png")

        self.label.setPixmap(QtGui.QPixmap("harry159821@126.com.png"))        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    windows = Windows()
    windows.show()
    sys.exit(app.exec_())
    # image = Image.open("harry159821@126.com.png")
    # # image.save("harry159821@126.com.png.jpg","jpeg")
    # image.save("harry159821@126.com.png","png")
