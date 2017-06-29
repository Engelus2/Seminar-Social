import steamapi
from steamapi.user import SteamGroup
import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

userByFriends = {}
userByFriends2 = {}
userByFriendsall = {}
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByFriends2 = JsonHelper.loadJson(userByFriends2, 'SortFriend50000_2.txt')

for x in userByFriends:
	for y in userByFriends[x]:
		setinDictionary(userByFriendsall,x,y)
for x in userByFriends2:
	for y in userByFriends2[x]:
		setinDictionary(userByFriendsall,x,y)
GamesByUserStatistik = {}
GamesByUserStatistik = JsonHelper.loadJson(GamesByUserStatistik, 'UserGamesStatistik.txt')
GamesByUserFriends = {}
UserByNumberOfGames = {}
counter = 0
for x in GamesByUserStatistik:
	friends = 0.0
	setinDictionary(UserByNumberOfGames,int(x),len(GamesByUserStatistik[x]))
	for y in GamesByUserStatistik[x]:
		try:
			friends += len(userByFriendsall[str(y)])
		except:
			counter += 1
	friends = friends/len(GamesByUserStatistik[x])
	setinDictionary(GamesByUserFriends,int(x),friends)
JsonHelper.printJson(GamesByUserFriends, 'UserbyNumberofGamesFriends.txt')
JsonHelper.printJson(UserByNumberOfGames, 'NumberOfGamesStatistik.txt')
print(counter)
