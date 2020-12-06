import sys
import json


def isValid(filename):
    data = open(filename)
    loadedData = json.load(data)
    valid = 0
    for i in loadedData:
        if (len(i) == 8) or (len(i) == 7 and 'cid' not in i):
            valid += 1
    print (valid)
                                      
if __name__ == "__main__":
    args = sys.argv
    isValid(args[1])
    