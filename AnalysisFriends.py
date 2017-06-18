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
userByFriendsall = {}
userByFriends = JsonHelper.loadJson(userByFriends, 'SortFriend50000.txt')
userByFriends2 = JsonHelper.loadJson(userByFriends2, 'SortFriend50000_2.txt')
for x in userByFriends:
	for y in userByFriends[x]:
		setinDictionary(userByFriendsall,x,y)
for x in userByFriends2:
	for y in userByFriends2[x]:
		setinDictionary(userByFriendsall,x,y)
maxvalue=0.0
people=0.0
meanvalue=0.0
alladded=0.0
for x in userByFriendsall:
	number = len(userByFriendsall[x])
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
'''
temp = 0.0
for x in NumberOfFriendsStatistik:
	temp += NumberOfFriendsStatistik[x][0]
	print(temp)
'''
for i in NumberOfFriends:
	value = 0.0
	people = 0.0
	for j in NumberOfFriends[i]:
		innervalue = 0.0
		innerpeople = 0.0
		for k in userByFriendsall[j]:
			try:
				if len(userByFriendsall[str(j)]) == 3:
					print(i,value,people,j,str(j),innervalue,innerpeople,k,str(k),len(userByFriendsall[str(k)]),len(userByFriendsall[str(j)]))
				innervalue+=len(userByFriendsall[str(k)])
				innerpeople += 1
			except:
				innervalue=innervalue
		if innerpeople !=0:
			innervalue = innervalue/innerpeople
			value += innervalue
			people += 1
	value = value/people
	setinDictionary(NumberOfFriendsFriends,i,value)
JsonHelper.printJson(NumberOfFriendsFriends, 'NumberOfFriendsFriends.txt')
