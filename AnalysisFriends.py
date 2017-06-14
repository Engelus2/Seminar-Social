import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

NumberOfFriendsFriends = {}
NumberOfFriends = {}
NumberOfFriendsStatistik = {}
userByFriends = {}
userByFriends2 = {}
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByFriends2 = JsonHelper.loadJson(userByFriends2, 'SortFriend50000_2.txt')
for x in userByFriends2:
	for y in userByFriends2[x]:
		setinDictionary(userByFriends,x,y)
maxvalue=0.0
people=0.0
meanvalue=0.0
alladded=0.0
for x in userByFriends:
	number = len(userByFriends[x])
	people+=1
	alladded+=number
	if number>maxvalue:
		maxvalue=number
	setinDictionary(NumberOfFriends,number,x)
for i in NumberOfFriends:
	setinDictionary(NumberOfFriendsStatistik,i,len(NumberOfFriends[i]))
meanvalue=(alladded/people)
print("max: "+str(maxvalue))
print("mean: "+str(meanvalue))
print("people: "+str(people))
print("all: "+str(alladded))
hit = False
for i in range(1,2000):
	if not hit:
		if i not in NumberOfFriendsStatistik: 
			hit = True
			print("geringste nicht vorhandene Anzahl an Freunden: "+str(i))
JsonHelper.printJson(NumberOfFriends, 'NumberOfFriends.txt')
JsonHelper.printJson(NumberOfFriendsStatistik, 'NumberOfFriendsStatistik.txt')
for i in NumberOfFriends:
	value = 0.0
	alle = 0.0
	insidedone=0.0
	for x in NumberOfFriends[i]:
		invalue = 0.0
		people = 0.0
		print(i,len(NumberOfFriends),"INSIDE",insidedone,len(NumberOfFriends[i]))
		for y in userByFriends[x]:	
			for a in NumberOfFriends:
				if str(y) in NumberOfFriends[a]:
					invalue+=a
					people+=1
		if people != 0:
			invalue=invalue/people
			alle+=1
		value+=invalue
		insidedone+=1
	value=value/alle
	setinDictionary(NumberOfFriendsFriends,i,value)
JsonHelper.printJson(NumberOfFriendsFriends, 'NumberOfFriendsFriends.txt')
