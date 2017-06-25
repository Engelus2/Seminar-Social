import steamapi
from steamapi.user import SteamGroup
import JsonHelper
import datetime, time
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

userByLastlogoff = {}
userByTimecreated = {}
userByYear = {}
userByYearNumber = {}
userByYearFriends = {}

userByLastlogoff = JsonHelper.loadJson(userByLastlogoff, 'SortLastlogoff50000.txt')
userByTimecreated = JsonHelper.loadJson(userByTimecreated, 'SortTimecreated50000.txt')
youngest = 0.0
oldest = 100000000000.0
people = 0.0
average = 0.0
t = datetime.datetime(1970,1,1)
drei = (datetime.datetime(2003,1,1)-t).total_seconds()
vier = (datetime.datetime(2004,1,1)-t).total_seconds()
for x in userByTimecreated:
	temp = float(str(x))
	people += 1
	average += temp
	user = userByTimecreated[x][0]
	start = 2003
	windowfront = drei
	windowback = vier
	nothit = True
	while(nothit):
		if temp > windowfront and temp < windowback:
			setinDictionary(userByYear,start,user)
			nothit=False
		else:
			windowfront += (vier-drei)
			windowback += (vier-drei)
			start += 1
	if temp < oldest:
		oldest = float(str(x))
	if temp > youngest:
		youngest = float(str(x))

average=average/people
print(int(oldest),int(youngest))
print(datetime.datetime.fromtimestamp(int(oldest)))
print(datetime.datetime.fromtimestamp(int(youngest)))
print(datetime.datetime.fromtimestamp(int(average)))
JsonHelper.printJson(userByYear, 'UserYearCreated.txt')
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
for x in userByYear:
	setinDictionary(userByYearNumber,x,len(userByYear[x]))
	people = 0.0
	friends = 0.0
	for y in userByYear[x]:
		try:
			friends += len(userByFriendsall[str(y)])
			people += 1
		except:
			people = people
	friends = friends/people
	setinDictionary(userByYearFriends,x,friends)
JsonHelper.printJson(userByYearNumber, 'NumberUserYear.txt')
JsonHelper.printJson(userByYearFriends, 'FriendsUserYear.txt')

