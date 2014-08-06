from PyQt4 import QtGui,QtCore
from PyQt4.QtDeclarative import QDeclarativeView

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    view = QDeclarativeView()
    view.setSource(QtCore.QUrl.fromLocalFile("main.qml"))
    view.show()
    
    # widget = QtGui.QWidget()
    # layout = QtGui.QVBoxLayout(widget)
    # layout.addWidget(view)

    # widget.show()
    sys.exit(app.exec_())
