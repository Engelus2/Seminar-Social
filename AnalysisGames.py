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
GamesByUsers1 = {}
GamesByUsers2 = {}
GamesByUsers3 = {}
GamesByUsers4 = {}
UserGamesStatistik = {}
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

counter = 0
for x in userByGames1:
	counter += 1
	print(1,counter,len(userByGames1))
	for y in userByGames1[x]:
		setinDictionary(userByGamesall,x,y)
counter = 0
for x in userByGames2:
	counter += 1
	print(2,counter,len(userByGames2))
	for y in userByGames2[x]:
		setinDictionary(userByGamesall,x,y)
counter = 0
for x in userByGames3:
	counter += 1
	print(3,counter,len(userByGames3))
	for y in userByGames3[x]:
		setinDictionary(userByGamesall,x,y)
counter = 0
for x in userByGamesall:
	counter += 1
	print(4,counter,len(userByGamesall))
	for y in userByGamesall[x]:	
		setinDictionary(GamesByUsers,y,x)
counter = 0
for x in GamesByUsers:
	print(5,counter, len(GamesByUsers))
	setinDictionary(UserGamesStatistik,x,len(GamesByUsers[x]))
counter = 0
for x in GamesByUsers:
	counter+=1
	print(6,counter, len(GamesByUsers))
	if counter%4==0:
		for y in GamesByUsers[x]:
			setinDictionary(GamesByUsers1,x,y)
	if counter%4==1:
		for y in GamesByUsers[x]:
			setinDictionary(GamesByUsers2,x,y)
	if counter%4==2:
		for y in GamesByUsers[x]:
			setinDictionary(GamesByUsers3,x,y)
	if counter%4==3:
		for y in GamesByUsers[x]:
			setinDictionary(GamesByUsers4,x,y)
JsonHelper.printJson(GamesByUsers1, 'UserGames_1.txt')
print("DONE with writing first splitted list")
JsonHelper.printJson(GamesByUsers2, 'UserGames_2.txt')
print("DONE with writing second splitted list")
JsonHelper.printJson(GamesByUsers3, 'UserGames_3.txt')
print("DONE with writing third splitted list")
JsonHelper.printJson(GamesByUsers4, 'UserGames_4.txt')
print("DONE with writing splitted lists")
JsonHelper.printJson(UserGamesStatistik, 'UserGamesStatistik.txt')
print("DONE with writing statistik")
JsonHelper.printJson(GamesByUsers, 'UserGames.txt')
print("DONE")
