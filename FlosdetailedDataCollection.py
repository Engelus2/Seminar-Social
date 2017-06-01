
import steamapi
from steamapi.user import SteamGroup
import JsonHelper
import datetime, time
import json

#steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True) 
steamapi.core.APIConnection(api_key="3FF94A9C0C8E7833E315736F735CE048", validate_key=True)

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

def goThroughList(list):
    counter = 0
    for x in list:
	print(counter)
	counter = counter +1
	if x not in usedPlayers:
		me = steamapi.user.SteamUser(userid = x)
		if me.privacy == 3:
		    if me.country_code is None:
			setinDictionary(userByCountry, 'null', me.steamid)
		    else:
			setinDictionary(userByCountry, me.country_code, me.steamid)
		    setinDictionary(userByLevel, str(me.level), me.steamid)
		    if me.is_community_banned is False:
		    	setinDictionary(userByCommunityBan, 'false', me.steamid)
		    else:
		    	setinDictionary(userByCommunityBan, 'true', me.steamid)
	 	    setinDictionary(userByLastlogoff, str((me.last_logoff-t).total_seconds()), me.steamid)
	 	    setinDictionary(userByTimecreated, str((me.time_created-t).total_seconds()), me.steamid)
		    for y in me.games:
		        setinDictionary(userByGames, y.name, me.steamid)
		    for y in me.recently_played:
		        setinDictionary(userByRecentlyplayed, y.name, me.steamid)
		    for y in me.friends:
		        setinDictionary(userByFriends, str(me.steamid), y.steamid)
		    if me.is_vac_banned is False:
		    	setinDictionary(userByVACBan, 'false', me.steamid)
		    else:
		    	setinDictionary(userByVACBan, 'true', me.steamid)

def getRidOfAlreadyDone():
	for i in userByVACBan:
		for x in userByVACBan[i]:
			usedPlayers.append(x)
	

PlayerList = []
userByCountry = {}
userByFriends = {}
userByLevel = {}
userByVACBan = {}
userByCommunityBan = {}
userBySteamID = {}
userByGames = {}
userByLastlogoff = {}
userByTimecreated = {}
userByRecentlyplayed = {}
usedPlayers = []
t = datetime.datetime(1970,1,1)

userBySteamID = JsonHelper.loadJson(userBySteamID, 'PlayerList.txt')

#'''
userByCountry = JsonHelper.loadJson(userByCountry, 'SortCountry50000.txt')
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByLevel = JsonHelper.loadJson(userByLevel, 'SortLevel50000.txt')
userByVACBan = JsonHelper.loadJson(userByVACBan, 'SortVACBan50000.txt')
userByCommunityBan = JsonHelper.loadJson(userByCommunityBan, 'SortCommunityBan50000.txt')
userByGames = JsonHelper.loadJson(userByGames, 'SortGames50000.txt')
userByLastlogoff = JsonHelper.loadJson(userByLastlogoff, 'SortLastlogoff50000.txt')
userByTimecreated = JsonHelper.loadJson(userByTimecreated, 'SortTimecreated50000.txt')
userByRecentlyplayed = JsonHelper.loadJson(userByRecentlyplayed, 'SortRecentlyplayed50000.txt')
#'''

try:
    PlayerList = userBySteamID['players']
    getRidOfAlreadyDone()
    goThroughList(PlayerList)
except:	
	print('X')

JsonHelper.printJson(userByFriends, 'SortFriend50000.txt')
JsonHelper.printJson(userByLevel, 'SortLevel50000.txt')
JsonHelper.printJson(userByCommunityBan, 'SortCommunityBan50000.txt')
JsonHelper.printJson(userByGames, 'SortGames50000.txt')
JsonHelper.printJson(userByRecentlyplayed, 'SortRecentlyplayed50000.txt')
JsonHelper.printJson(userByLastlogoff, 'SortLastlogoff50000.txt')
JsonHelper.printJson(userByTimecreated, 'SortTimecreated50000.txt')
JsonHelper.printJson(userByCountry, 'SortCountry50000.txt')
JsonHelper.printJson(userByVACBan, 'SortVACBan50000.txt')
print('Z')
