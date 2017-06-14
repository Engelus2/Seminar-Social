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
