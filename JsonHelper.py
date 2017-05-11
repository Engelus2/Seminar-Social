

import json
def printJson(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        