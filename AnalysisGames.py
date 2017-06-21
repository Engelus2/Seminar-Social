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
userByGames1 = {}
userByGames2 = {}
userByGames3 = {}
userByGamesall = {}
GamesByUsers = {}
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByFriends2 = JsonHelper.loadJson(userByFriends2, 'SortFriend50000_2.txt')
userByGames1 = JsonHelper.loadJson(userByGames1, 'SortGames50000.txt')
userByGames2 = JsonHelper.loadJson(userByGames2, 'SortGames50000_2.txt')
userByGames3 = JsonHelper.loadJson(userByGames3, 'SortGames50000_3.txt')

for x in userByFriends:
	for y in userByFriends[x]:
		setinDictionary(userByFriendsall,x,y)
for x in userByFriends2:
	for y in userByFriends2[x]:
		setinDictionary(userByFriendsall,x,y)

for x in userByGames1:
	print("1",x)
	for y in userByGames1[x]:
		setinDictionary(userByGamesall,x,y)
for x in userByGames2:
	print("2",x)
	for y in userByGames2[x]:
		setinDictionary(userByGamesall,x,y)
for x in userByGames3:
	print("3",x)
	for y in userByGames3[x]:
		setinDictionary(userByGamesall,x,y)

for x in userByGamesall:
	print(x)
	for y in userByGamesall[x]:	
		setinDictionary(GamesByUsers,y,x)
JsonHelper.printJson(GamesByUsers, 'UserGames.txt')
