'''
Created on Feb 19, 2015

@author: akira
'''
from PyQt4.Qt import QThread,pyqtSignal
from coreutil.connectionUtils import DataGeneratorImage,DataGeneratorJson
from __builtin__ import str
class ThreadGetJson(QThread):
    jsonready = pyqtSignal(dict)
    imgready = pyqtSignal(str)
    empty = pyqtSignal()
    def __init__(self,title):
        QThread.__init__(self)
        self.title = title
    def run(self):
        data = self.returndata(self.title)
        if data is None:
            self.empty.emit()
        else:
            self.jsonready.emit(data)
            imgda = DataGeneratorImage()
            imglocation = imgda.getImage(data)
            if not imglocation == None:
                self.imgready.emit(imglocation)
    
    def returndata(self,title):
        emitdata = DataGeneratorJson()
        data = emitdata.getDataByTitle(title)
        if not 'Error' in data:
            return data
        

        