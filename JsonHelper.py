
import json
import jsonpickle

def printJson(data, file):
    with open(file, 'w') as outfile:
        #json.dump(json.loads(jsonpickle.encode(data)), outfile, sort_keys=True, indent=4, separators=(',', ': '))
        json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
def loadJson(data, file):
    with open(file) as data_file:    
        data = json.load(data_file)
    return data

def printJson2(data, file):
    with open(file, 'w') as outfile:
        json.dump(json.loads(jsonpickle.encode(data)), outfile, sort_keys=True, indent=4, separators=(',', ': '))
        