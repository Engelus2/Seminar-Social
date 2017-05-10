import steamapi
from userProfile import *
import json
import io
steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True)
# me = steamapi.user.SteamUser(userurl="smileybarry")  # For http://steamcommunity.com/id/smileybarrysmileybarry

listDone = []
listToDo = []

listToDo.append(76561197996416028) # ID von smileybarry
counter = 0
for i in range(0,5):
    me = steamapi.user.SteamUser(userid=listToDo[0])
    if(me.privacy == 3):
        newuser = userProfile()
        newuser.id = me.steamid
        for x in me.friends:
            newuser.friendslist.append(x.steamid)
            if x.steamid not in listToDo and x.steamid not in listDone:
                listToDo.append(x.steamid)
                counter+=1
        listDone.append(newuser)

    del listToDo[0]
print(counter)

for x in listDone:
    print(x.id)
    print(x.friendslist[0])
    print("---------")

data={'stuff':listDone}

def jdefault(o):
    return o.__dict__
with open('data.txt', 'w') as outfile:
    str = json.dumps(listDone, outfile, default=jdefault)
    outfile.write(str)
    outfile.close
