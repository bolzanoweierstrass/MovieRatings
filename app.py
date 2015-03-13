'''
Created on Jan 15, 2015

@author: akira
'''
from ravan.mymain import MymainWindow
from PyQt4 import QtGui
import sys 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MymainWindow()
    window.show()
    sys.exit(app.exec_())