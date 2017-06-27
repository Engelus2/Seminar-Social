import JsonHelper
import networkx as nx
import time

class User():
    
    def __init__(self, id, comBan, country, lastlogOff, level, privacy, recPlayed, timeCreated, vacBan, numFriends, friends):
        self.id = id
        self.comBan = comBan
        self.country = country
        self.lastlogOff = lastlogOff
        self.level = level
        self.privacy = privacy
        self.recPlayed = recPlayed
        self.timeCreated = timeCreated
        self.vacBan = vacBan
        self.numFriends = numFriends
        self.friends = friends

def getVariable(dict, id):
    for key, value in dict.items():
        if(id in value):
            return key
    return 'null'

friends = {}
friends2 = {}
comBan = {}
country = {}
lastlogOff = {}
level = {}
privacy = {}
recPlayed = {}
timeCreated = {}
vacBan = {}
numFriends = {}
onlyAnalyzedFriends = {}
games = {}
games2 = {}
games3 = {}
userGames = {}
userGames2 = {}
userGames3 = {}
userGames4 = {}


# Jsons die bereits eingelesen wurden
friends = JsonHelper.loadJson(friends, '../Data/SortFriend50000.txt')
friends2 = JsonHelper.loadJson(friends2, '../Data/SortFriend50000_2.txt')
comBan = JsonHelper.loadJson(comBan, '../Data/SortCommunityBan50000.txt')
country = JsonHelper.loadJson(country, '../Data/SortCountry50000.txt')
lastlogOff = JsonHelper.loadJson(lastlogOff, '../Data/SortLastlogoff50000.txt')
level = JsonHelper.loadJson(level, '../Data/SortLevel50000.txt')
privacy = JsonHelper.loadJson(privacy, '../Data/SortPrivacy50000.txt')
recPlayed = JsonHelper.loadJson(recPlayed, '../Data/SortRecentlyplayed50000.txt')
timeCreated = JsonHelper.loadJson(timeCreated, '../Data/SortTimecreated50000.txt')
vacBan = JsonHelper.loadJson(vacBan, '../Data/SortVACBan50000.txt')
numFriends = JsonHelper.loadJson(numFriends, '../Data/NumberOfpersonalFriends.txt')
onlyAnalyzedFriends = JsonHelper.loadJson(onlyAnalyzedFriends, '../Data/onlyAnalyzedFriends.txt')

#games = JsonHelper.loadJson(games, '../Data/SortGames50000.txt')
games2 = JsonHelper.loadJson(games2, '../Data/SortGames50000_2.txt')
games3 = JsonHelper.loadJson(games3, '../Data/SortGames50000_3.txt')
userGames = JsonHelper.loadJson(userGames, '../Data/UserGames_1.txt')
userGames2 = JsonHelper.loadJson(userGames2, '../Data/UserGames_2.txt')
userGames3 = JsonHelper.loadJson(userGames3, '../Data/UserGames_3.txt')
userGames4 = JsonHelper.loadJson(userGames4, '../Data/UserGames_4.txt')
for x in friends2:
    friends[x] = friends2[x]
    
for x in games2:
    games[x] = games2[x]
for x in games3:
    games[x] = games3[x] 
       
for x in userGames2:
    userGames[x] = userGames2[x]
for x in userGames3:
    userGames[x] = userGames3[x]    
for x in userGames4:
    userGames[x] = userGames4[x]    




def getTroughDictInGraph(dict, G, name):
    for key in dict:
        for id in dict[key]:
            try:
                G.node[int(id)][name] = key
            except:
                print "need to vrate"
                #G.add_node(int(id))
                #G.node[int(id)][name] = key
                #if key == "DE": 
                    #print "de"
                    
                    

def addAttribute(G, node, name, att):
    G.node[node][name] = att

def getFriendsConnectionGraph(user, G):
    if str(user) in onlyAnalyzedFriends:
        for friend in onlyAnalyzedFriends[str(user)]:
            G.add_edge(int(user), int(friend))

'''
for user in friends:
    list = []
    for friend in friends[str(user)]:
        if str(friend) in friends:
            list.append(friend)
            print "fsa"
    onlyAnalyzedFriends[user] = list
JsonHelper.printJson(onlyAnalyzedFriends, 'onlyAnalyzedFriends.txt')
'''
print "start Graph"
start = time.clock()
G = nx.Graph()

'''
print "read"
G = nx.read_gml('../GML/graph.gml')
print "end read"

'''
for x in privacy[str(3)]:
    G.add_node(int(x))
    G.node[int(x)]['type'] = "user"
    
getTroughDictInGraph(comBan, G, 'comBan')
getTroughDictInGraph(country, G, 'country')
getTroughDictInGraph(lastlogOff, G, 'lastlogOff')
getTroughDictInGraph(level, G, 'level')
#getTroughDictInGraph(privacy, G, 'privacy')
getTroughDictInGraph(recPlayed, G, 'recPlayed')
getTroughDictInGraph(timeCreated, G, 'timeCreated')
getTroughDictInGraph(vacBan, G, 'vacBan')
print "converted"

for x in games:
    print x
    print x.encode('utf-8', 'ignore').decode('utf-8')
    G.node[str(x)]['type'] = "game"
print len(games)
len =  len(userGames)
print len
counter = 0.0
for x in userGames:
    print counter / len
    counter +=1
    for y in userGames[x]:
        G.add_edge(int(x), y)
print "ende" + time.clock() - start
nx.write_gml(G, '../GML/graphGames.gml')
print time.clock() - start

'''
    
    
         
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