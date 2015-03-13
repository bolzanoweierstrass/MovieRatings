'''
Created on Jan 15, 2015

@author: akira
'''
from guimain.aboutwindow import Ui_Form
from PyQt4 import QtGui

class MyAboutWindow(QtGui.QWidget,Ui_Form):
    def __init__(self,parent=QtGui.QMainWindow):
        QtGui.QWidget.__init__(self,parent=None)
        self.setupUi(self)
        self.connectsignals()
    def connectsignals(self):
        self.tBn_credits.clicked.connect(self.showCredits)
        self.tBn_about.clicked.connect(self.makecheck)
    def makecheck(self):
        self.stackedWidget.setCurrentIndex(0)
    def showCredits(self):
        self.stackedWidget.setCurrentIndex(1)


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance
        
        