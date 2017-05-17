#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 03.05.2017

@author: Alexander



Kommentare (rechtschreibfehler bitte behalten)

Kurze erklaerung
stopRequestAt anzahl der nutzer die ihr analysieren wollts
beim starten:
    mit eingabe 1 bekommts ihr den fortschritt (gebts eine andere Zahl ein so verschwindert er wieder)
    mit eingabe 9 beendet ichr das Programm (json wird trotzdem erstellt wie weit er halt gekommen ist)


Das ist eine Test klasse also definitiv nicht optimal aber erf�llt den zweck


'''

import steamapi
import time
from steamapi.user import SteamGroup
import JsonHelper
import networkx as nx
import matplotlib.pyplot as plt
from thread import start_new_thread

'''
Diesen wert setzten Achtung es entspricht nicht der Wirklichen anzahl da manche user doppelt gez�hlt werden
zB bei 50000 kommen etwa 40000 nutzer raus (wie schon gesagt der code ist eher zweckmae�ig als logisch)
'''
stopRequestAt = 500

threadcontroll = 0
currentrequest = 0
steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True)  # <-- Insert API key here
startuser = steamapi.user.SteamUser(76561197960279154)
users = [startuser]
usersByCountry = {}
userByFriends = {}

G = nx.Graph()

'''
setzt den Wert value in die Liste des Dictionary beim Schluessel key ein
'''
def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

'''
geht ein bisschen verwirrend durch freunde solange bis stopRequesAt angekommen ist
'''
def goThrougFriends(user):
    global currentrequest
    friendList = user.friends
    id = user.steamid
    currentrequest += len(friendList)
    global threadcontroll
    for i in friendList:
        if i not in users:
            users.append(i)
            setinDictionary(usersByCountry, i.country_code, i.steamid)
            setinDictionary(userByFriends, id, i.steamid)
            if threadcontroll == 1:
                print len(users)
                print "find ID " ,currentrequest / float(stopRequestAt)
                print "sort ID: " ,len(users) / float(currentrequest)
            if currentrequest < stopRequestAt and i.privacy == 3:
                goThrougFriends(i)
    print "ende"  
    
def getFriendsConnectionGraph(user):
    if user.privacy == 3:
        for i in user.friends:
            if i.privacy == 3:
                G.add_edge(user.steamid, i.steamid)
    else:
        print "notublic"
    
    
         
getFriendsConnectionGraph(startuser)
lenge = len(startuser.friends)
counter = 0
for x in startuser.friends:
    counter +=1
    print counter/ float (lenge)
    getFriendsConnectionGraph(x)
nx.draw(G)
plt.show()
'''
start = time.time() 

try:
    start_new_thread(getFriendsConnectionGraph, (startuser, ))

except:
    print "vorzeitiges Ende"
while threadcontroll is not 9:
    threadcontroll = int(input("Ihre Eingabe? "))

end = time.time()
# eigentlich nichtssagend  
print "Time: ", (end - start)

print len(users)
JsonHelper.printJson(usersByCountry, 'SortCountry.txt')
JsonHelper.printJson(userByFriends, 'SortFriend.txt')
'''