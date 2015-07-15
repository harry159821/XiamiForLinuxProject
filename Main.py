#!/usr/bin/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore,Qt
import sys
import mainWindows
import loginWindows
import xiamiApi

'''
Xiami For Linux Project
'''
class XiamiPlayer(object):
    def __init__(self):
        super(XiamiPlayer, self).__init__()
        self.app = QtGui.QApplication(sys.argv)
                
        self.loginWindow = loginWindows.LoginWindows()
        self.loginWindow.inputEnd.connect(self.loginInputEnd)
        self.loginWindow.validateInputEnd.connect(self.loginValidateInputEnd)
        self.loginWindow.show()

        # Run
        sys.exit(self.app.exec_())

    def loginValidateInputEnd(self,validate):
        self.result = self.session.loginValidate(validate)

        if self.result == "needValidate":
            self.loginWindow.inputValidate()
        elif self.result == "emailPwdError":
            self.loginWindow.emailPwdError()
        elif self.result == "loginSuccess":
            print "loginSuccess"
        elif self.result == "noMailPwd":
            pass        

    def loginInputEnd(self,mail,pwd):        
        self.session = xiamiApi.loginSession(mail,pwd)
        self.result = self.session.tryLogin()

        if self.result == "needValidate":
            self.loginWindow.inputValidate()
        elif self.result == "emailPwdError":
            self.loginWindow.emailPwdError()
        elif self.result == "loginSuccess":
            print "loginSuccess"
            self.mainWinow = mainWindows.MainWindow()
            self.loginWindow.close()
            self.mainWinow.show()
        elif self.result == "noMailPwd":
            pass

if __name__ == '__main__':
    xiamiPlayer = XiamiPlayer()
