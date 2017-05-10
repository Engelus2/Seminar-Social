'''
Created on 03.05.2017

@author: Alexander
'''

import steamapi
from steamapi.user import SteamGroup

stopRequestAt = 100 
currentrequest = 0
steamapi.core.APIConnection(api_key="153823DBBAD57AE1360496D35A75FDC0", validate_key=True)  # <-- Insert API key here
startuser = steamapi.user.SteamUser(76561197960279154)
friends = startuser.friends
users = [startuser]
usersByCountry = {}


def setinDictionary(dict, key, value):
    if key in dict:
        if value not in dict[key]:
            dict[key].append(value)
    else:
        dict[key] = [value]


def goThrougFrtiends(friendList):
    global currentrequest
    currentrequest += len(friendList)
    for i in friendList:
        if i not in users:
            users.append(i)
            setinDictionary(usersByCountry, i.country_code, i)
            if currentrequest < stopRequestAt and i.privacy == 3:
                goThrougFrtiends(i.friends)
  
goThrougFrtiends(startuser.friends)
if "DE" in usersByCountry:
    print "DE"
    print usersByCountry["DE"]
print len(users)
