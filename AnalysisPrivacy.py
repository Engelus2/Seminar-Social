import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

userByPrivacy = {}
userByPrivacyNumber = {}
userByPrivacy = JsonHelper.loadJson(userByPrivacy, 'SortPrivacy50000.txt')
for x in userByPrivacy:
	setinDictionary(userByPrivacyNumber,x,len(userByPrivacy[x]))
JsonHelper.printJson(userByPrivacyNumber, 'FrequencyofPrivacyTypes.txt')
