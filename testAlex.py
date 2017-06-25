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
friends = JsonHelper.loadJson(friends, 'FlosData/SortFriend50000.txt')
friends2 = JsonHelper.loadJson(friends2, 'FlosData/SortFriend50000_2.txt')
comBan = JsonHelper.loadJson(comBan, 'FlosData/SortCommunityBan50000.txt')
country = JsonHelper.loadJson(country, 'FlosData/SortCountry50000.txt')
lastlogOff = JsonHelper.loadJson(lastlogOff, 'FlosData/SortLastlogoff50000.txt')
level = JsonHelper.loadJson(level, 'FlosData/SortLevel50000.txt')
privacy = JsonHelper.loadJson(privacy, 'FlosData/SortPrivacy50000.txt')
recPlayed = JsonHelper.loadJson(recPlayed, 'FlosData/SortRecentlyplayed50000.txt')
timeCreated = JsonHelper.loadJson(timeCreated, 'FlosData/SortTimecreated50000.txt')
vacBan = JsonHelper.loadJson(vacBan, 'FlosData/SortVACBan50000.txt')
numFriends = JsonHelper.loadJson(numFriends, 'FlosData/NumberOfpersonalFriends.txt')
onlyAnalyzedFriends = JsonHelper.loadJson(onlyAnalyzedFriends, 'onlyAnalyzedFriends.txt')

for x in friends2:
    friends[x] = friends2[x]

users = {}
'''
print users
c = 0
for us in friends:
    c +=1 
    print us
    users[us] = User(us, getVariable(comBan,us), getVariable(country,us) , getVariable(lastlogOff,us), getVariable(level,us), getVariable(privacy,us), getVariable(recPlayed,us), getVariable(timeCreated,us), getVariable(vacBan,us), getVariable(numFriends,us), getVariable(friends,us))
    if c == 10:
        break;

'''
'''
def getFriendsConnectionGraph(dictFriends, users):
    counter = 0.0
    
    for x in dictFriends:
        if(x in users):
            G.add_node(x, comBan=users[x].comBan, country=users[x].country, lastlogOff=users[x].lastlogOff,
                        level=users[x].level, privacy=users[x].privacy, recPlayed=users[x].recPlayed, 
                        timeCreated=users[x].timeCreated, vacBan=users[x].vacBan, numFriends=users[x].numFriends)
            print counter/len(dictFriends)
            counter +=1.0
            for y in dictFriends[x]:
                if(y in G.nodes()):
                    G.add_edge(x, y)
            if(counter == 20):
                return;
'''

def getTroughDictInGraph(dict, G, name):
    for key in dict:
        for id in dict[key]:
            try:
                G.node[int(id)][name] = key
            except:
                if key == "DE": 
                    print "de"
                    print "need to vrate"
                    G.add_node(int(id))
                    G.node[int(id)][name] = key
                    

                    

def getFriendsConnectionGraph(user, G):
    if str(user) in friends:
        for friend in friends[str(user)]:
            if int(friend) in G.nodes():
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

G = nx.Graph()

print "se"
#G = nx.read_gml("graph.gml")
#G.add_node(76561197971506367, test='5pm')
getTroughDictInGraph(comBan, G, 'comBan')
getTroughDictInGraph(country, G, 'country')
getTroughDictInGraph(lastlogOff, G, 'lastlogOff')
getTroughDictInGraph(level, G, 'level')
getTroughDictInGraph(privacy, G, 'privacy')
getTroughDictInGraph(recPlayed, G, 'recPlayed')
getTroughDictInGraph(timeCreated, G, 'timeCreated')
getTroughDictInGraph(vacBan, G, 'vacBan')

start = time.clock()

counter = 0.0
anz = len(G.nodes())
for node in G.nodes():
    counter +=1
    getFriendsConnectionGraph(node, G)
    print counter / anz

print time.clock() - start
nx.write_gml(G, 'graphDE.gml')
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