import steamapi
from steamapi.user import SteamGroup
import JsonHelper
import time

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

listDone = []
listToDo = []
usersByCountry = {}
userByFriends = {}
userByLevel = {}
userByVACBan = {}
userByCommunityBan = {}
userBySteamID = {}
steamapi.core.APIConnection(api_key="3FF94A9C0C8E7833E315736F735CE048", validate_key=True)
me = steamapi.user.SteamUser(userurl = 'smileybarry')  # For http://steamcommunity.com/id/smileybarrysmileybarry
stoprequestat = 50000

listToDo.append(me) # ID von smileybarry
setinDictionary(userBySteamID, 'players', me.steamid)

def goThroughFriends(notDone):
    while notDone:
        me = steamapi.user.SteamUser(userid=listToDo[0].steamid)
        if(me.privacy == 3):
            #setinDictionary(usersByCountry, me.country_code, me.steamid)
            #setinDictionary(userByLevel, me.level, me.steamid)
	    #setinDictionary(userByVACBan, me.is_vac_banned, me.steamid)
	    #setinDictionary(userByCommunityBan, me.is_community_banned, me.steamid)
            for x in me.friends:
                #if x not in listToDo and x.steamid not in listDone:
                    #setinDictionary(userByFriends, me.steamid, x.steamid)
                    listToDo.append(x)
		    setinDictionary(userBySteamID, 'players', x.steamid)
                    #if x.privacy == 3:
                         #setinDictionary(usersByCountry, x.country_code, x.steamid)
			
            listDone.append(me.steamid)
        del listToDo[0]
	if(len(userBySteamID['players']))>=stoprequestat:
		notDone = False;
        print "Players searched: ",len(listDone)
        print "IDs collected: " ,len(userBySteamID['players'])	


start=time.time()
try:
	goThroughFriends(True)

except Exception, e:
	print("DONE; DONE; DONE")
	print(e)

'''
for x in listToDo:
	print(counter)
	counter = counter-1
	listDone.append(x.steamid)
	setinDictionary(usersByCountry, x.country_code, x.steamid)
	if(x.privacy == 3):
		setinDictionary(userByLevel, x.level, x.steamid)
	    	setinDictionary(userByVACBan, x.is_vac_banned, x.steamid)
	    	setinDictionary(userByCommunityBan, x.is_community_banned, x.steamid)
		for i in x.friends:
			if i.steamid in listDone:
				setinDictionary(userByFriends, x.steamid, i.steamid)
				setinDictionary(userByFriends, i.steamid, x.steamid)
'''
end = time.time()
    
print(end-start)
JsonHelper.printJson(userBySteamID, 'PlayerList.txt')
'''
JsonHelper.printJson(userByCountry, 'SortCountryBig.txt')
JsonHelper.printJson(userByFriends, 'SortFriendBig.txt')
JsonHelper.printJson(userByLevel, 'SortLevelBig.txt')
JsonHelper.printJson(userByVACBan, 'SortVACBanBig.txt')
JsonHelper.printJson(userByCommunityBan, 'SortCommunityBanBig.txt')
'''
