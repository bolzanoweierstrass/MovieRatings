'''
Created on Jan 12, 2015

@author: akira
'''
import requests,os
import tempfile
class DataGeneratorJson(object):
    def __init__(self):
        self._url = 'http://omdbapi.com/'
        self.payload = {'r':'json','plot':'short','tomatoes':'true'}
    
    def getDataByTitle(self,title,plot="short"):
        try:
            if self.payload.has_key('s'):del self.payload['s']
            if plot == "long": self.payload.update({'plot':'full'})
        finally:
            self.payload.update({'t':title})
            req = requests.get(self._url, params = self.payload)
            data = req.json()
            return data
    
    def getDataBySearch(self,title):
        try:
            if self.payload.has_key('t'):del self.payload['t']
        finally:
            self.payload.update({'s':title})
            req = requests.get(self._url,params = self.payload)
            data = req.json()
            return data
class DataGeneratorImage(object):
    def getImage(self,data):
        if data.has_key('Poster'):
            poster = data['Poster']
            localdir = tempfile.gettempdir()
            tempimage = os.path.join(localdir,poster.split('/')[-1])
            req = requests.get(poster, stream=True)
            with open(tempimage, 'w+b') as infile:
                for chunk in req.iter_content(2*1024):
                    if chunk:
                        infile.write(chunk)
                        infile.flush()
            return tempimage
        else:
            pass
            
        
        
        