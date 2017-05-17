import steamapi
from steamapi.user import SteamGroup
import JsonHelper
from thread import start_new_thread
import time

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
steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True)
me = steamapi.user.SteamUser(userurl="smileybarry")  # For http://steamcommunity.com/id/smileybarrysmileybarry
stoprequestat = 10
threadcontroll = 0

listToDo.append(me) # ID von smileybarry
counter = 0

start = time.time() 

for i in range(1,stoprequestat+1):
    me = steamapi.user.SteamUser(userid=listToDo[0].steamid)
    if(me.privacy == 3):
        setinDictionary(usersByCountry, me.country_code, me.steamid)
	setinDictionary(userByLevel, me.level, me.steamid)
        for x in me.friends:
            if x.steamid not in listToDo and x.steamid not in listDone:
		setinDictionary(userByFriends, me.steamid, x.steamid)
                listToDo.append(x)
                counter+=1
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
end = time.time()

print(counter)
print(end-start)

JsonHelper.printJson(usersByCountry, 'SortCountry.txt')
JsonHelper.printJson(userByFriends, 'SortFriend.txt')
JsonHelper.printJson(userByLevel, 'SortLevel.txt')
