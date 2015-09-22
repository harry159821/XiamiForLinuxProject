#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
import sys,os
import mainWindows
import loginWindows
import xiamiApi

'''
Xiami For Linux Project
'''
class XiamiPlayer(QtCore.QObject):
    def __init__(self):
        super(XiamiPlayer, self).__init__()
        self.app = QtGui.QApplication(sys.argv)

        self.settings = QtCore.QSettings("setting.ini", QtCore.QSettings.IniFormat)

            
        if self.settings.value('XiamiPlayer/cachePath',"") != "":
            self.cachePath = self.settings.value('XiamiPlayer/cachePath',"").toString()
        else:
            self.settings.setValue('XiamiPlayer/cachePath',"./cache/")
            self.cachePath = "./cache/"

        self.loginWindow = loginWindows.LoginWindows()
        self.loginWindow.inputEnd.connect(self.loginInputEnd)
        self.loginWindow.validateInputEnd.connect(self.loginValidateInputEnd)
        self.loginThread = LoginThread()
        self.loginThread.loginOver.connect(self.checkLogin)
        self.loginWindow.show()

        self.loginWindow.setMailPwd(self.settings.value('XiamiPlayer/usermail',""),
            self.settings.value('XiamiPlayer/pwd',""))

        headfilename = (self.session.cachePath + self.session.usermail + '.png').toUtf8().data()
        print headfilename
        if os.path.exists(headfilename) and os.path.getsize(headfilename) > 0:
            self.loginWindow.headLabel.setPixmap(QtGui.QPixmap(headfilename))
        else:
            self.loginWindow.headLabel.setPixmap(QtGui.QPixmap("default_user.ico"))                

        # self.mainWinow = mainWindows.MainWindow()
        # self.mainWinow.show()

        # Run
        sys.exit(self.app.exec_())

    def loginValidateInputEnd(self,validate):
        self.loginThread.loginValidate(self.session,validate)

    def loginInputEnd(self,mail,pwd):
        print "self.cachePath:",self.cachePath
        self.session = xiamiApi.loginSession(mail,pwd,self.cachePath)
        self.loginThread.login(self.session)
        
    def checkLogin(self,result):
        self.result = result
        if self.result == "needValidate":
            self.loginWindow.inputValidate()
        elif self.result == "emailPwdError":
            self.loginWindow.emailPwdError()
        elif self.result == "loginSuccess":
            self.loginSuccess()
        elif self.result == "noMailPwd":
            self.loginWindow.emailPwdError()

    def loginSuccess(self):
        self.settings.setValue('XiamiPlayer/usermail',self.session.usermail)
        self.settings.setValue('XiamiPlayer/pwd',self.session.password)

        headfilename = (self.session.cachePath + self.session.usermail + '.png').toUtf8().data()
        print headfilename
        if os.path.exists(headfilename) and os.path.getsize(headfilename) > 0:
            pass    
        else:
            headfilename = self.session.downloadUserHead(usermail=self.session.usermail)
        self.loginWindow.headLabel.setPixmap(QtGui.QPixmap(headfilename))

        self.mainWinow = mainWindows.MainWindow()
        self.loginWindow.close()
        self.mainWinow.show()

class LoginThread(QtCore.QThread):
    loginOver = QtCore.pyqtSignal(str)
    def __init__(self):
        super(LoginThread, self).__init__()
        self.mutex = QtCore.QMutex()
        self.loginFlag = False
        self.loginValidateFlag = False

    def login(self,session):
        self.mutex.lock()
        self.session = session
        self.mutex.unlock()
        self.loginFlag = True        
        if not self.isRunning():
            self.start(QtCore.QThread.LowPriority)

    def loginValidate(self,session,validate):
        self.mutex.lock()
        self.session = session
        self.validate = validate
        self.mutex.unlock()
        self.loginValidateFlag = True
        if not self.isRunning():
            self.start(QtCore.QThread.LowPriority)

    def run(self):
        if self.loginFlag:
            self.loginFlag = False
            self.result = self.session.tryLogin()
            self.loginOver.emit(self.result)

        if self.loginValidateFlag:
            self.loginValidateFlag = False
            self.result = self.session.loginValidate(self.validate)
            self.loginOver.emit(self.result)

if __name__ == '__main__':
    xiamiPlayer = XiamiPlayer()
