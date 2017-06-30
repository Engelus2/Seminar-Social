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

userbyNGF = {}
userbyNGF = JsonHelper.loadJson(userbyNGF, 'UserbyNumberofGamesFriends.txt')
userbyNGS = {} 
userbyNGS = JsonHelper.loadJson(userbyNGS, 'NumberOfGamesStatistik.txt')
userByNGames = {}
tvalue = 0.0
tpeople = 0
fvalue = 0.0
fpeople = 0
zvalue = 0.0
zpeople = 0
dvalue = 0.0
dpeople = 0
vvalue = 0.0
vpeople = 0
for x in userbyNGS:
	if int(x) < 200:
		setinDictionary(userByNGames,int(x),userbyNGF[x][0])
	else:
		if int(x) > 999:
			tvalue += userbyNGF[x][0]*userbyNGS[x][0]
			tpeople += userbyNGS[x][0]
		else:
			if int(x) > 499:
				fvalue += userbyNGF[x][0]*userbyNGS[x][0]
				fpeople += userbyNGS[x][0]
			else:
				if int(x) < 300:
					zvalue += userbyNGF[x][0]*userbyNGS[x][0]
					zpeople += userbyNGS[x][0]
				else:
					if int(x) < 400:
						dvalue += userbyNGF[x][0]*userbyNGS[x][0]
						dpeople += userbyNGS[x][0]
					else:
						vvalue += userbyNGF[x][0]*userbyNGS[x][0]
						vpeople += userbyNGS[x][0]

tvalue=tvalue/tpeople
setinDictionary(userByNGames,int(1000),float(tvalue))
fvalue=fvalue/fpeople
setinDictionary(userByNGames,int(500),float(fvalue))
zvalue=zvalue/zpeople
setinDictionary(userByNGames,int(200),float(zvalue))
dvalue=dvalue/dpeople
setinDictionary(userByNGames,int(300),float(dvalue))
vvalue=vvalue/vpeople
setinDictionary(userByNGames,int(400),float(vvalue))
JsonHelper.printJson(userByNGames, 'UserbyNumberofGamesFriends_grouped.txt')
