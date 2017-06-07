import cPickle as pickle
import steamapi
from steamapi.user import SteamGroup


class Data(object):
    def __init__(self):
        self.dictPrivate = {}
        self.dictDone = {}
        self.dictToDo = {}

    def addUser(self, id):
        me = steamapi.user.SteamUser(userid=id)
        self.dictDone[me.steamid] = me   
        if(me.privacy == 3):
            self.dictPrivate[me.steamid] = me 
            for x in me.friends:
                self.dictToDo[x.steamid] = x 
                if x.privacy == 3:
                    self.dictPrivate[x.steamid] = x            
    
    
    def addXUsers(self, count):
        while count>0:
            me = steamapi.user.SteamUser(userid=self.dictToDo.keys()[0])
            print count
            if me.steamid not in self.dictDone:
                count -=1
                self.dictDone[me.steamid] = me 
                if(me.privacy == 3):
                    self.dictPrivate[me.steamid] = me 
                    for x in me.friends:
                        self.dictToDo[x.steamid] = x  
                        if x.privacy == 3:
                            self.dictPrivate[x.steamid] = x      
            del self.dictToDo[me.steamid]
    
    def addUntilXPrivateUsers(self, count):
        while count>=len(self.dictPrivate):
            me = steamapi.user.SteamUser(userid=self.dictToDo.keys()[0])
            if me.steamid not in self.dictDone:
                self.dictDone[me.steamid] = me 
                if(me.privacy == 3):
                    self.dictPrivate[me.steamid] = me 
                    for x in me.friends:
                        self.dictToDo[x.steamid] = x
                        if x.privacy == 3:
                            self.dictPrivate[x.steamid] = x             
            del self.dictToDo[me.steamid]
    

    
def saveItl(obj, filename):
    with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def loadIt(filename):
    with open(filename, 'rb') as input:
        obj = pickle.load(input)
        return obj