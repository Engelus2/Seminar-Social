import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

NumberOfCitizens = {}
userByCountry = {}
userByCountry = JsonHelper.loadJson(userByCountry, 'SortCountry50000.txt')
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
'''
maxvalue=0.0
people=0.0
meanvalue=0.0
alladded=0.0
for x in userByCountry:
	number = len(userByCountry[x])
	people+=1
	alladded+=number
	if number>maxvalue:
		maxvalue=number
	setinDictionary(NumberOfCitizens,x,number)
meanvalue=(alladded/people)
print("max: "+str(maxvalue))
print("mean: "+str(meanvalue))
print("countrys: "+str(people))
print("all: "+str(alladded))
JsonHelper.printJson(NumberOfCitizens, 'NumberOfCitizens.txt')
'''
FriendsbyCountry = {}
FriendsbyCountry10p = {}
PercentageInternational = {}
PercentageInternational10p = {}
counter=0
'''
DE = 0
inte = 0
nul = 0

for a in userByCountry["DE"]:
	try:
		for x in userByFriends[str(a)]:
			if x in userByCountry["DE"]:
				DE +=1
				#print("DE",DE)
			else:
				if x in userByCountry["null"]:
					nul +=1
					#print("null",nul)
				else:
					for y in userByCountry:
						if x in userByCountry[y]:
							inte+=1
							#print(y,inte)
	except:
		counter=0
print(inte,(inte+DE+nul))
'''
for x in userByCountry:
	counter+=1
	value = 0.0
	people = 0.0
	international = 0.0
	nulp = 0.0
	innerland=0.0
	innercounter=0.0
	for y in userByCountry[x]:
		innercounter+=1
		print(innercounter,len(userByCountry[x]),x,counter,len(userByCountry))
		try:
			value += len(userByFriendsall[str(y)])
			people+=1
		except:
			value=value
		try:
			for z in userByFriendsall[str(y)]:
				if z in userByCountry[x]:
					innerland+=1
				else:
					if z in userByCountry["null"]:
						nulp +=1
					else:
						for q in userByCountry:
							if z in userByCountry[q]:
								international+=1
		except:
			counter = counter
	print(x,international,nulp,innerland)
	if people != 0:
		value = value/people
		setinDictionary(FriendsbyCountry,x,value)
	if people > 9:
		setinDictionary(FriendsbyCountry10p,x,value)
	try:
		international = international/(international+nulp+innerland)
		setinDictionary(PercentageInternational,x,international)
	except:
		international = international
	if len(userByCountry[x]) > 9:
		setinDictionary(PercentageInternational10p,x,international)
JsonHelper.printJson(FriendsbyCountry, 'NumberOfFriendsbyCountry.txt')
JsonHelper.printJson(FriendsbyCountry10p, 'NumberOfFriendsbyCountry10plus.txt')
JsonHelper.printJson(PercentageInternational, 'PercentageOfInternationalFriends.txt')
JsonHelper.printJson(PercentageInternational10p, 'PercentageOfInternationalFriends10plus.txt')
