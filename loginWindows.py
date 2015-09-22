#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore,Qt
from PyQt4.QtDeclarative import QDeclarativeView
import renderCircle

class LoginForm(object):
    def setupUi(self, Form):
        
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        # self.verticalLayoutWidget.resize(400, 270)
        # Form.setCentralWidget(self.verticalLayoutWidget)

        self.widget = QtGui.QWidget(Form)
        # self.widget = renderCircle.RenderCircleWidget(self)

        self.layout = QtGui.QVBoxLayout()
        self.widget.setLayout(self.layout)
        # self.layout.addWidget(self.verticalLayoutWidget)
        Form.setCentralWidget(self.widget)
       
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 300, 160))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

        self.font = QtGui.QFont()
        self.font.setPixelSize(14)   # 设置字号32,以像素为单位
        self.font.setFamily("SimSun")# 设置字体，宋体
        self.font.setFamily(u"微软雅黑")
        # self.font.setWeight(20)    # 设置字型,不加粗
        self.font.setBold(True)
        self.font.setItalic(False)   # 设置字型,不倾斜
        self.font.setUnderline(False)# 设置字型,无下划线
        self.setFont(self.font)     
    
        self.verticalLayout.setMargin(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.mailLabel = QtGui.QLabel('Usermail:',self.verticalLayoutWidget)
        self.horizontalLayout.addWidget(self.mailLabel)
        self.mailEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout.addWidget(self.mailEdit)
        
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.pwdLabel = QtGui.QLabel("Password:",self.verticalLayoutWidget)
        self.horizontalLayout_4.addWidget(self.pwdLabel)
        self.pwdEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_4.addWidget(self.pwdEdit)        

        self.validateImgLayout = QtGui.QHBoxLayout()
        self.validateImg = QtGui.QLabel("ValidateImg")
        self.validateImgLayout.addWidget(self.validateImg)        

        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.validateLabel = QtGui.QLabel('Validate:  ',self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.validateLabel)
        self.validateEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.validateEdit)
        
        # self.verticalLayout.addWidget(self.headLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.validateImgLayout)   
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        # self.pwdEdit.setMaxLength()

        self.horizontalLayout.setContentsMargins(40,0,40,0)
        self.horizontalLayout_2.setContentsMargins(40,0,40,40)
        self.horizontalLayout_4.setContentsMargins(40,0,40,0)
        self.validateImgLayout.setContentsMargins(125,10,50,0)
        self.verticalLayout.setContentsMargins(0,20,0,0)

        self.mailEdit.setTextMargins(10,0, 10,0)
        self.pwdEdit.setTextMargins(10,0, 10,0)        
        self.validateEdit.setTextMargins(10,100, 10,100)

        # self.font.setPixelSize(14)
        # self.mailEdit.setFont(self.font)
        # self.pwdEdit.setFont(self.font)
        # self.validateEdit.setFont(self.font)

        self.headLabel = QtGui.QLabel(self)
        # self.headLabel.set
        # self.headPixmap = QtGui.QPixmap("default_user.ico")
        # self.headPixmap.scaled (10,10,
        #     QtCore.Qt.IgnoreAspectRatio,
        #     QtCore.Qt.FastTransformation
        #     )
        # self.headLabel.setPixmap(self.headPixmap)
        self.headLabel.setScaledContents(True)
        self.headLabel.resize(70,70)
        self.headLabel.move(145,10)
        
        Form.resize(350+0*2,250-40)
        self.layout.setContentsMargins(0,40,0, 0)
        # self.layout.setContentsMargins(40,40,40,40)
        self.layout.addWidget(self.verticalLayoutWidget)

        self.verticalLayoutWidget.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint|QtCore.Qt.FramelessWindowHint)
        self.widget.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint|QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.X11BypassWindowManagerHint|QtCore.Qt.FramelessWindowHint)

        self.verticalLayoutWidget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # self.widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

class LoginWindows(QtGui.QMainWindow,LoginForm):
    inputEnd = QtCore.pyqtSignal(str,str)
    validateInputEnd = QtCore.pyqtSignal(str) 
    def __init__(self):
        super(LoginWindows, self).__init__()
        self.setObjectName("LoginWindows")        
        self.setupUi(self)
        # #1f282e
        # background-color:#454e58;
        self.setStyleSheet(''' 
        LoginWindows {
            background-color: #454e58;
        }
        .QWidget {
            border-radius:9px;
            min-width: 350px;   
            min-height: 200px;
            padding-top: 0px;
        }
        QLineEdit {
            height: 21px;
            min-width: 190px;   
            max-width: 190px;
            min-height: 21px;
            max-height: 21px;
            padding: -5px;
            border: 7px;          
            border-image: url("img/nav_srch_input.png");
        }
        QLabel{
            color:orange;
        }
            ''')
        # border-image: url("img/nav_srch_input.png");
        # border-image: url("Resources/xmslider_track_high.tiff");

        self.showPwd()

        self.mailEdit.editingFinished.connect(self.mailEditEnd)
        self.pwdEdit.editingFinished.connect(self.pwdEditEnd)
        self.validateEdit.editingFinished.connect(self.validateEnd)
        self.inputEndFlag = False
        self.inputValidateEndFlag = False

        self.desktop = QtGui.QApplication.desktop()
        self.center(1)

    def center(self,screenNum=0):
        '''多屏居中支持'''
        screen = self.desktop.availableGeometry(screenNum)
        size = self.geometry()
        self.normalGeometry2 = QtCore.QRect((screen.width()-size.width())/2+screen.left(),
                         (screen.height()-size.height())/2,
                         size.width(),size.height())
        self.setGeometry((screen.width()-size.width())/2+screen.left(),
                         (screen.height()-size.height())/2,
                         size.width(),size.height())

    def validateEnd(self):
        if self.validateEdit.text():
            if not self.inputValidateEndFlag:
                self.inputValidateEndFlag = True
                self.validateEdit.setEnabled(False)
                self.validateInputEnd.emit(self.validateEdit.text())

    def mailEditEnd(self):
        self.mail = self.mailEdit.text()
        if self.mail:
            self.pwdEdit.setFocus()

    def setMailPwd(self,mail="",pwd=""):
        self.mail = mail.toString()
        self.pwd = pwd.toString()
        if self.mail:
            if self.pwd:
                self.mailEdit.setText(self.mail)
                self.pwdEdit.setText(self.pwd)
                self.pwdEditEnd()
            else:
                self.mailEdit.setText(self.mail)
                self.mailEditEnd()

    def pwdEditEnd(self):
        self.pwd = self.pwdEdit.text()
        if self.pwd:
            if self.mail:
                if not self.inputEndFlag:                    
                    self.inputEndFlag = True
                    self.mailEdit.setEnabled(False)
                    self.pwdEdit.setEnabled(False)
                    # inputOver
                    self.inputEnd.emit(self.mail,self.pwd)
            else:
                # mail not input
                self.mailEdit.setFocus()

    def inputValidate(self):
        self.inputValidateEndFlag = False
        self.validateEdit.setEnabled(True)
        self.validateEdit.clear()
        self.validateEdit.setFocus()
        self.validateImg.setPixmap(QtGui.QPixmap("Captcha.png"))
        self.showValidate()

    def emailPwdError(self):
        self.mailEdit.clear()
        self.pwdEdit.clear()
        self.mailEdit.setEnabled(True)
        self.pwdEdit.setEnabled(True)        
        self.mailEdit.setFocus()
        self.showPwd()

    def showValidate(self):
        self.horizontalLayout_2.setContentsMargins(40,0,40,40)
        self.validateLabel.setVisible(True);self.validateEdit.setVisible(True)
        self.validateImg.setVisible(True)
        self.mailLabel.setVisible(False);self.mailEdit.setVisible(False);
        self.pwdLabel.setVisible(False);self.pwdEdit.setVisible(False);

    def showPwd(self):
        self.horizontalLayout_2.setContentsMargins(40,0,40,0)
        self.inputEndFlag = False
        self.validateLabel.setVisible(False);self.validateEdit.setVisible(False)
        self.validateImg.setVisible(False)
        self.mailLabel.setVisible(True);self.mailEdit.setVisible(True);
        self.pwdLabel.setVisible(True);self.pwdEdit.setVisible(True);

class Test(QtGui.QWidget):
    def __init__(self):
        super(Test, self).__init__()
        self.resize(500,400)
        self.show()        
        self.setWindowOpacity(0.9)

    def paintEvent(self,event):
        painter = QtGui.QPainter(self)       
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(235,45,211),QtCore.Qt.SolidPattern))
        painter.setPen(QtGui.QPen(QtGui.QColor(218,92,202),9))
        painter.drawEllipse(20,20,100,100)        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    windows = LoginWindows()
    windows.show()
    # windows.validateImg.setPixmap(QtGui.QPixmap("Captcha.png"))
    # windows.showValidate()

    # test = Test()
    windows.headLabel.setPixmap(QtGui.QPixmap("cache/harry159821@126.com.png"))

    sys.exit(app.exec_())
