
import steamapi
from steamapi.user import SteamGroup
import JsonHelper

steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True) 
#steamapi.core.APIConnection(api_key="3FF94A9C0C8E7833E315736F735CE048", validate_key=True)

listIDs = [76561197996416028,
        76561197960279154,
        76561197961699727,
        76561197962475589,
        76561197967396871,
        76561197967707835,
        76561197968371098,
        76561197969676484]
userByCountry = {}
userByFriends = {}
userByLevel = {}
userByVACBan = {}
userByCommunityBan = {}
userBySteamID = {}
userByGames = {}


    
def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

def goThroughList(list):
    counter = -1
    for x in list:
        counter = counter +1
        print counter
        me = steamapi.user.SteamUser(userid = x)
        if me.privacy == 3:
            setinDictionary(userByCountry, me.country_code, me.steamid)
            setinDictionary(userByLevel, me.level, me.steamid)
            setinDictionary(userByVACBan, me.is_vac_banned, me.steamid)
            setinDictionary(userByCommunityBan, me.is_community_banned, me.steamid)
            for y in me.games:
                setinDictionary(userByGames, y.name, me.steamid)
            
            '''
            for y in me.friends:
                setinDictionary(userByFriends, me.steamid, y.steamid)
            '''


temp = {}
temp = JsonHelper.loadJson(temp, 'PlayerList.txt')

try:
    goThroughList(temp['players'])
except:
    print "irgendeinen scheiss"
JsonHelper.printJson(userByCountry, 'SortCountryBig.txt')
JsonHelper.printJson(userByFriends, 'SortFriendBig.txt')
JsonHelper.printJson(userByLevel, 'SortLevelBig.txt')
JsonHelper.printJson(userByVACBan, 'SortVACBanBig.txt')
JsonHelper.printJson(userByCommunityBan, 'SortCommunityBanBig.txt')
JsonHelper.printJson(userByGames, 'SortGamesBig.txt')
