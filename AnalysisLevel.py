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
userByLevel = {}
userByLevel = JsonHelper.loadJson(userByLevel, 'SortLevel50000.txt')
friendsbyLevel = {}
LevelCounter = {}
for x in userByLevel:
	value = 0.0
	people = 0
	setinDictionary(LevelCounter,int(x),len(userByLevel[x]))
	for y in userByLevel[x]:
		try:
			value += len(userByFriendsall[str(y)])
			people += 1
		except:
			people = people
	value = value/people
	setinDictionary(friendsbyLevel,int(x),value)
friendsbyLevel2 = {}
hvalue = 0.0
hpeople = 0
fvalue = 0.0
fpeople = 0
svalue = 0.0
speople = 0
vvalue = 0.0
vpeople = 0
evalue = 0.0
epeople = 0
nvalue = 0.0
npeople = 0
for x in friendsbyLevel:
	if x < 51:
		setinDictionary(friendsbyLevel2,int(x),friendsbyLevel[x][0])
	if x > 100:
		hvalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		hpeople += userByLevel[str(x)][0]
	if x > 50 and x < 61:
		fvalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		fpeople += userByLevel[str(x)][0]
	if x > 60 and x < 71:
		svalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		speople += userByLevel[str(x)][0]
	if x > 70 and x < 81:
		vvalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		vpeople += userByLevel[str(x)][0]
	if x > 80 and x < 91:
		evalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		epeople += userByLevel[str(x)][0]
	if x > 90 and x < 101:
		nvalue += friendsbyLevel[x][0]*userByLevel[str(x)][0]
		npeople += userByLevel[str(x)][0]

hvalue = hvalue/hpeople
setinDictionary(friendsbyLevel2,int(101),hvalue)
fvalue = fvalue/fpeople
setinDictionary(friendsbyLevel2,int(51),fvalue)
svalue = svalue/speople
setinDictionary(friendsbyLevel2,int(61),svalue)
vvalue = vvalue/vpeople
setinDictionary(friendsbyLevel2,int(71),vvalue)
evalue = evalue/epeople
setinDictionary(friendsbyLevel2,int(81),evalue)
nvalue = nvalue/npeople
setinDictionary(friendsbyLevel2,int(91),hvalue)
JsonHelper.printJson(friendsbyLevel2, 'FriendsbyLevel_grouped.txt')
JsonHelper.printJson(friendsbyLevel, 'FriendsbyLevel.txt')
JsonHelper.printJson(LevelCounter, 'LevelStatistik.txt')
