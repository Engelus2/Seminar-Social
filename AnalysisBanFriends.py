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
userByVACBan = {}
userByCommunityBan = {}
userByVACBan = JsonHelper.loadJson(userByVACBan, 'SortVACBan50000.txt')
userByCommunityBan = JsonHelper.loadJson(userByCommunityBan, 'SortCommunityBan50000.txt')
userByBan = {}
for x in userByFriendsall:
	if int(x) not in userByVACBan["true"] and int(x) not in userByCommunityBan["true"]:
		setinDictionary(userByBan,"none",int(x))
	if int(x) not in userByVACBan["true"] and int(x) in userByCommunityBan["true"]:
		setinDictionary(userByBan,"Community",int(x))
	if int(x) in userByVACBan["true"] and int(x) not in userByCommunityBan["true"]:
		setinDictionary(userByBan,"VAC",int(x))
	if int(x) in userByVACBan["true"] and int(x) in userByCommunityBan["true"]:
		setinDictionary(userByBan,"both",int(x))
JsonHelper.printJson(userByBan, 'SortBan50000.txt')
userByBanPercentage = {}
for x in userByBan:
	people=0.0
	banned=0.0
	counter=0
	for y in userByBan[x]:
		counter += 1
		print(x,counter,len(userByBan[x]))
		try:
			for z in userByFriendsall[str(y)]:
				if z in userByVACBan["true"] or z in userByCommunityBan["true"]:
					people += 1
					banned += 1
				if z in userByVACBan["false"] and z in userByCommunityBan["false"]:
					people += 1
		except:
			people=people
	banned = banned/people
	setinDictionary(userByBanPercentage,x,banned)
JsonHelper.printJson(userByBanPercentage, 'PercentageBannedFriends.txt')
