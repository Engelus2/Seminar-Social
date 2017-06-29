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


GamesByUser1 = {}
GamesByUser2 = {}
GamesByUser3 = {}
GamesByUser4 = {}
GamesByUserStatistik = {}
GamesByUserFriends = {}
maximum = 0.0
minimum = 100000000000.0
people = 0.0
average = 0.0
counter = 0
GamesByUser1 = JsonHelper.loadJson(GamesByUser1, 'UserGames_1.txt')
for x in GamesByUser1:
	print(counter,len(GamesByUser1))
	counter += 1
	setinDictionary(GamesByUserStatistik,len(GamesByUser1[x]),x)
	people+=1
	average+=len(GamesByUser1[x])
	if len(GamesByUser1[x]) > maximum:
		maximum = len(GamesByUser1[x])
	if len(GamesByUser1[x]) < minimum:
		minimum = len(GamesByUser1[x])
print("Loaded 1")
counter = 0
GamesByUser2 = JsonHelper.loadJson(GamesByUser2, 'UserGames_2.txt')
for x in GamesByUser2:
	print(counter,len(GamesByUser2))
	counter += 1
	setinDictionary(GamesByUserStatistik,len(GamesByUser2[x]),x)
	people+=1
	average+=len(GamesByUser2[x])
	if len(GamesByUser2[x]) > maximum:
		maximum = len(GamesByUser2[x])
	if len(GamesByUser2[x]) < minimum:
		minimum = len(GamesByUser2[x])
print("Loaded 2")
counter = 0
GamesByUser3 = JsonHelper.loadJson(GamesByUser3, 'UserGames_3.txt')
for x in GamesByUser3:
	print(counter,len(GamesByUser3))
	counter += 1
	setinDictionary(GamesByUserStatistik,len(GamesByUser3[x]),x)
	people+=1
	average+=len(GamesByUser3[x])
	if len(GamesByUser3[x]) > maximum:
		maximum = len(GamesByUser3[x])
	if len(GamesByUser3[x]) < minimum:
		minimum = len(GamesByUser3[x])
print("Loaded 3")
counter = 0
GamesByUser4 = JsonHelper.loadJson(GamesByUser4, 'UserGames_4.txt')
for x in GamesByUser4:
	print(counter,len(GamesByUser4))
	counter += 1
	setinDictionary(GamesByUserStatistik,len(GamesByUser4[x]),x)
	people+=1
	average+=len(GamesByUser4[x])
	if len(GamesByUser4[x]) > maximum:
		maximum = len(GamesByUser4[x])
	if len(GamesByUser4[x]) < minimum:
		minimum = len(GamesByUser4[x])
print("Loaded 4")

average = average/people
print(minimum)
print(maximum)
print(people)
print(average)
JsonHelper.printJson(GamesByUserStatistik, 'UserGamesStatistik.txt')
