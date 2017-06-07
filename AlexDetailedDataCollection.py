
import steamapi
from steamapi.user import SteamGroup
import JsonHelper
import SaveData
import datetime, time


#steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True) 
#steamapi.core.APIConnection(api_key="3FF94A9C0C8E7833E315736F735CE048", validate_key=True)

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

def goThroughDict(dict):
    counter = 0
    for me in dict.values():
        print counter
        counter = counter +1
        if me.privacy == 3:
            try:
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
                else:
                    print("False Friends")
            except:
                print('Something went wrong')    
                del dict[me.steamid]


    
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


try:
    data = SaveData.loadIt('SaveData.pkl')
except:
    print "No such file"
    #data = SaveData.Data()
    #data.addUser(76561197996416028)

'''
try:
    data.addXUsers(100)
except:    
    print('Error Users')

print '--------------'
'''

goThroughDict(data.dictPrivate)




SaveData.saveItl(data, 'SaveDataNew.pkl')

#War ein test ob die Datei kliener ist viel sogar groesser aus minimal
#SaveData.saveItl(data.dictDone.values()[0], 'SaveStartUser.pkl')



#JsonHelper.printJson2(data.dictPrivate, "AlexData/JsonAllData.txt")

print "jsons"
JsonHelper.printJson(userByFriends, 'AlexData/SortFriend.txt')
JsonHelper.printJson(userByLevel, 'AlexData/SortLevel.txt')
JsonHelper.printJson(userByCommunityBan, 'AlexData/SortCommunityBan.txt')
JsonHelper.printJson(userByGames, 'AlexData/SortGames.txt')
JsonHelper.printJson(userByRecentlyplayed, 'AlexData/SortRecentlyplayed.txt')
JsonHelper.printJson(userByLastlogoff, 'AlexData/SortLastlogoff.txt')
JsonHelper.printJson(userByTimecreated, 'AlexData/SortTimecreated.txt')
JsonHelper.printJson(userByCountry, 'AlexData/SortCountry.txt')
JsonHelper.printJson(userByVACBan, 'AlexData/SortVACBan.txt')

print('Z')
