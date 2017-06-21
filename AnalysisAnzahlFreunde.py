import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

NumberOfFriends = {}
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
for x in userByFriendsall:
	setinDictionary(NumberOfFriends, x, len(userByFriendsall[x]))
JsonHelper.printJson(NumberOfFriends, 'NumberOfpersonalFriends.txt')

