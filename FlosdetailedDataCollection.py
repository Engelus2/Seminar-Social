
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
    pcounter= 0
    falsefriends = 0
    wrong = 0
    pcountermax = 51000
    for x in list:
	try:
		
		if pcounter < pcountermax:
			print("This time: ", pcounter)
			print("total counter: ", counter)
			if x not in usedPlayers2:
				me = steamapi.user.SteamUser(userid = x)
				setinDictionary(userByPrivacy, str(me.privacy), me.steamid)
			if x not in usedPlayers:
				me = steamapi.user.SteamUser(userid = x)
				if me.country_code is None:
					setinDictionary(userByCountry, 'null', me.steamid)
				else:
					setinDictionary(userByCountry, me.country_code, me.steamid)
				if me.privacy == 3:
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
					pcounter = pcounter + 1
				
				else:
					falsefriends = falsefriends + 1
					print("False Friends: ", falsefriends)
		if pcounter < pcountermax:
			counter = counter +1
	except:
		wrong = wrong +1
		print("Something went wrong:", wrong)
    print("DONE getting data for now")
    print("counter: ", counter)
    print("This time: ", pcounter)
    print("False Friends: ", falsefriends)
    print("Something went wrong:", wrong)

def getRidOfAlreadyDone():
	for i in userByCountry:
		for x in userByCountry[i]:
			usedPlayers.append(x)
def getRidOfAlreadyDone2():
	for i in userByPrivacy:
		for x in userByPrivacy[i]:
			usedPlayers2.append(x)
def splitLists():
	    i = 0
	    for x in userByGames:
		if i%2 is 0:
			for y in userByGames[x]:
				setinDictionary(userByGames1, x, y)
		if i%2 is 1:
			for y in userByGames[x]:
				setinDictionary(userByGames2, x, y)
		print(i, len(userByGames1), len(userByGames2), len(userByGames))
	    	i = i+1
	    JsonHelper.printJson(userByGames1, 'SortGames50000.txt')
	    JsonHelper.printJson(userByGames2, 'SortGames50000_3.txt')
	    i = 0
	    for x in userByFriends:
		if i%2 is 0:
			for y in userByFriends[x]:
				setinDictionary(userByFriends1, x, y)
		if i%2 is 1:
			for y in userByFriends[x]:
				setinDictionary(userByFriends2, x, y)
		print(i, len(userByFriends1), len(userByFriends2), len(userByFriends))
	    	i = i+1
	    JsonHelper.printJson(userByFriends1, 'SortFriend50000.txt')
	    JsonHelper.printJson(userByFriends2, 'SortFriend50000_2.txt')
	
	

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
userByPrivacy = {}
userByGames1 = {}
userByGames2 = {}
userByFriends1 = {}
userByFriends2 = {}
usedPlayers = []
usedPlayers2 =[]
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
userByPrivacy = JsonHelper.loadJson(userByPrivacy, 'SortPrivacy50000.txt')
#'''

try:
    PlayerList = userBySteamID['players']
    getRidOfAlreadyDone()
    getRidOfAlreadyDone2()
    goThroughList(PlayerList)
    #splitLists()
except:	
	print('ERROR')

JsonHelper.printJson(userByFriends, 'SortFriend50000.txt')
JsonHelper.printJson(userByLevel, 'SortLevel50000.txt')
JsonHelper.printJson(userByCommunityBan, 'SortCommunityBan50000.txt')
JsonHelper.printJson(userByGames, 'SortGames50000.txt')
JsonHelper.printJson(userByRecentlyplayed, 'SortRecentlyplayed50000.txt')
JsonHelper.printJson(userByLastlogoff, 'SortLastlogoff50000.txt')
JsonHelper.printJson(userByTimecreated, 'SortTimecreated50000.txt')
JsonHelper.printJson(userByVACBan, 'SortVACBan50000.txt')
JsonHelper.printJson(userByCountry, 'SortCountry50000.txt')
JsonHelper.printJson(userByPrivacy, 'SortPrivacy50000.txt')
print("DONE")
