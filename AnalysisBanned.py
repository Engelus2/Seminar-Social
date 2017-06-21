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
userByVACBan = {}
userByCommunityBan = {}
FriendsbyVAC = {}
FriendsbyComBan = {}
userByVACBan = JsonHelper.loadJson(userByVACBan, 'SortVACBan50000.txt')
userByCommunityBan = JsonHelper.loadJson(userByCommunityBan, 'SortCommunityBan50000.txt')
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByFriends2 = JsonHelper.loadJson(userByFriends2, 'SortFriend50000_2.txt')
for x in userByFriends:
	for y in userByFriends[x]:
		setinDictionary(userByFriendsall,x,y)
for x in userByFriends2:
	for y in userByFriends2[x]:
		setinDictionary(userByFriendsall,x,y)
for x in userByVACBan:
	value = 0.0
	people = 0.0
	for y in userByVACBan[x]:
		try:
			value += len(userByFriendsall[str(y)])
			people += 1
		except:
			people=people
	value=value/people
	setinDictionary(FriendsbyVAC, x, value)
for x in userByCommunityBan:
	value = 0.0
	people = 0.0
	for y in userByCommunityBan[x]:
		try:
			value += len(userByFriendsall[str(y)])
			people += 1
		except:
			people=people
	value=value/people
	setinDictionary(FriendsbyComBan, x, value)

JsonHelper.printJson(FriendsbyVAC, 'FriendsbyVACBan.txt')
JsonHelper.printJson(FriendsbyComBan, 'FriendsbyCommunityBan.txt')
