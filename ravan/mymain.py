from guimain.mainwindow import Ui_MainWindow
from PyQt4 import QtGui
from ravan.myabout import MyAboutWindow
from utilsmain.Mythreads import ThreadGetJson
class MymainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.yabout = None
        self.connectSignals()
    
    def connectSignals(self):
        self.ui.actionAbout.triggered.connect(self.showinAbout)
        self.ui.tBn_search.clicked.connect(self.onBtnClicked)
        
    
    def onBtnClicked(self):
        self.clearall()
        title = str(self.ui.lne_url.text())
        self.thjson = ThreadGetJson(title)
        self.thjson.start()
        self.thjson.jsonready.connect(self.printit)
        self.thjson.empty.connect(self.sorry)
        self.thjson.imgready.connect(self.displayimg)
        
    def displayimg(self,location):
        mypix = QtGui.QPixmap(location)
        if not mypix.isNull():
            self.ui.lbl_pic.setPixmap(mypix)
    
    def printit(self,data):
        mykeys = ['Title','Actors','Writer','Director','Released','Type','Genre','Language','Country','Runtime','Awards','tomatoImage','tomatoMeter','imdbRating']
        for k in mykeys:
            self.ui.txtB_title.append(k+' ===>  '+data[k])
        self.ui.txtB_plot.append("plot" + "===>" + data['Plot'] + "\n")
        self.ui.txtB_plot.append("tomatoConsensus" + "====>" + data["tomatoConsensus"])
        
    def showinAbout(self):
        if self.yabout is None:
            self.yabout = MyAboutWindow(self)
        self.yabout.show()
    
    def clearall(self):
        self.ui.txtB_title.clear()
        self.ui.txtB_plot.clear()
        self.ui.lbl_pic.clear()
    def sorry(self):
        self.ui.txtB_title.append("we are sorry")
        mypix = QtGui.QPixmap(":/ico/errror.png")
        self.ui.lbl_pic.setPixmap(mypix)
        