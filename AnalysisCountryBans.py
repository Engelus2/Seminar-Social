import JsonHelper
import json

def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]

userByCountry = {}
userByCountry = JsonHelper.loadJson(userByCountry, 'SortCountry50000.txt')
userByVAC = {}
userByCommunity = {}
userByVAC = JsonHelper.loadJson(userByVAC, 'SortVACBan50000.txt')
userByCommunity = JsonHelper.loadJson(userByCommunity, 'SortCommunityBan50000.txt')
PercentageCountryVACBan = {}
PercentageCountryComBan = {}
PercentageCountryBan = {}
PercentageCountryVACBan40p = {}
PercentageCountryComBan40p = {}
PercentageCountryBan40p = {}
counter=0
for x in userByCountry:
	counter+=1
	print(x,counter,len(userByCountry))
	people = 0.0
	banVAC = 0.0
	banCom = 0.0
	fineVAC = 0.0
	fineCom = 0.0
	fineboth = 0.0
	for y in userByCountry[x]:
		people += 1
		if y in userByVAC["false"] and y in userByCommunity["false"]:
			fineboth += 1
			fineVAC += 1
			fineCom += 1
		else:
			if y in userByVAC["false"]:
				banCom += 1 
				fineVAC += 1
			else:
				banVAC += 1
				fineCom += 1
	fineboth = fineboth/people
	fineVAC = fineVAC/people
	fineCom = fineCom/people
	banVAC = banVAC/people
	banCom = banCom/people
	setinDictionary(PercentageCountryBan,x,(1-fineboth))
	setinDictionary(PercentageCountryComBan,x,(1-fineCom))
	setinDictionary(PercentageCountryVACBan,x,(1-fineVAC))
	if people > 39:
		setinDictionary(PercentageCountryBan40p,x,(1-fineboth))
		setinDictionary(PercentageCountryComBan40p,x,(1-fineCom))
		setinDictionary(PercentageCountryVACBan40p,x,(1-fineVAC))
JsonHelper.printJson(PercentageCountryBan, 'PercentageCountryBan.txt')
JsonHelper.printJson(PercentageCountryComBan, 'PercentageCountryComBan.txt')
JsonHelper.printJson(PercentageCountryVACBan, 'PercentageCountryVACBan.txt')
JsonHelper.printJson(PercentageCountryBan40p, 'PercentageCountryBan40plus.txt')
JsonHelper.printJson(PercentageCountryComBan40p, 'PercentageCountryComBan40plus.txt')
JsonHelper.printJson(PercentageCountryVACBan40p, 'PercentageCountryVACBan40plus.txt')
