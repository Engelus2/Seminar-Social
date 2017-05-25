import steamapi
from steamapi.user import SteamGroup
import JsonHelper
from thread import start_new_thread
import time
from random import random
import networkx as nx
import pylab as plt

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]
'''
'''

listDone = []
listToDo = []
usersByCountry = {}
userByFriends = {}
userByLevel = {}
steamapi.core.APIConnection(api_key="3FF94A9C0C8E7833E315736F735CE048", validate_key=True)
me = steamapi.user.SteamUser(userurl = 'smileybarry')  # For http://steamcommunity.com/id/smileybarrysmileybarry
stoprequestat = 500
threadcontroll = 0

listToDo.append(me) # ID von smileybarry
counter = 0
G = nx.Graph()
labels = {}
start = time.time() 
def goThroughFriends():
    global counter
    for i in range(1,stoprequestat+1):
        me = steamapi.user.SteamUser(userid=listToDo[0].steamid)
        labels[me.steamid]=me.country_code
        if(me.privacy == 3):
            setinDictionary(usersByCountry, me.country_code, me.steamid)
            #setinDictionary(userByLevel, me.level, me.steamid)

            for x in me.friends:
                if x.steamid not in listToDo and x.steamid not in listDone:
                    setinDictionary(userByFriends, me.steamid, x.steamid)
                    listToDo.append(x)
                    counter+=1
                    G.add_edge(me.steamid, x.steamid)
                    if x.privacy == 3:
                         setinDictionary(usersByCountry, x.country_code, x.steamid)
            listDone.append(me.steamid)
        del listToDo[0]
        print len(listDone)
        print(i)
        print "done-IDs: " ,i / float(stoprequestat)
        print "IDs left: " ,len(listToDo)

'''
for x in listToDo:
	setinDictionary(usersByCountry, x.country_code, x.steamid)
	if(x.privacy == 3):	
		setinDictionary(userByLevel, x.level, x.steamid)
'''


try:
	goThroughFriends()
except:
	print("DONE; DONE; DONE")
end = time.time()
    
print(counter)
print(end-start)
pos=nx.spring_layout(G)

temp = []
for x in listToDo:
    temp.append(x.steamid)

nx.draw_networkx_nodes(G, pos, nodelist=temp, node_color='b')
nx.draw_networkx_edges(G,pos)
#nx.draw_networkx_nodes(G, pos, nodelist=listDone, node_color='r')


for x in usersByCountry:
    colors = (random(), random(), random())
    print usersByCountry[x]
    nx.draw_networkx_nodes(G, pos, nodelist=usersByCountry[x], node_color = colors)    

#nx.draw_networkx_nodes(G, pos, nodelist=[me.steamid], node_color='g')
nx.draw_networkx_labels(G, pos, labels)


plt.show()

JsonHelper.printJson(usersByCountry, 'SortCountry.txt')
JsonHelper.printJson(userByFriends, 'SortFriend.txt')
JsonHelper.printJson(userByLevel, 'SortLevel.txt')

