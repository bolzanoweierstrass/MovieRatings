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
    def __init__(self,title,conditions):
        QThread.__init__(self)
        self.title = title
        self.conditions = conditions
    def run(self):
        data = self.returndata(self.title,self.conditions)
        if data is None:
            self.empty.emit()
        else:
            self.jsonready.emit(data)
            print(data)
            imgda = DataGeneratorImage()
            imglocation = imgda.getImage(data)
            if not imglocation == None:
                self.imgready.emit(imglocation)
    
    def returndata(self,title,conditions):
        
        if conditions == 0:
            emitdata = DataGeneratorJson()
            data = emitdata.getDataByTitle(title)
            if not data is None:
                if not 'Error' in data:
                    return data
        elif conditions == 1:
            emitdata = DataGeneratorJson()
            data = emitdata.getDataBySearch(title)
            if not data is None:
                if not "Error" in data:
                    return data

        