import steamapi
steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True)
# me = steamapi.user.SteamUser(userurl="smileybarry")  # For http://steamcommunity.com/id/smileybarrysmileybarry

listDone = []
listToDo = []

listToDo.append(76561197996416028) # ID von smileybarry
counter = 0
for i in range(0,9):
    me = steamapi.user.SteamUser(userid=listToDo[0])
    if(me.privacy == 3):
        for x in me.friends:
            if x.steamid not in listToDo and x.steamid not in listDone:    
                listToDo.append(x.steamid)
                counter+=1
        listDone.append(listToDo[0])
    del listToDo[0]
print(counter)
