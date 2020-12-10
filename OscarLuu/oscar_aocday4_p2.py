import sys
import json
import re

def byr(val):
    return (int(val) in range(1920, 2003))

def iyr(val):
    return (int(val) in range(2010, 2021))

def eyr(val):
    return (int(val) in range(2020, 2031))

def hgt(val):
    height = ''.join(i for i in val if i.isdigit())
    if 'cm' in val:
        return (height in range(150, 194))
    if 'in' in val:
        return (height in range(59, 77))
    
def hcl(val):
    return (bool(re.match('^#[a-f0-9]{6}$', val)))

def ecl(val):
    color = ["amb","blu","brn","gry","grn","hzl","oth"]
    return (val in color)

def pid(val):
    return (bool(re.match('^[0-9]{9}$', val)))

def cid(val):
    return True

dispatchTable = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': cid,
}

def handler(values):
    state = True
    for k,v in values.items():
        state = dispatchTable[k](v)
        # Troubleshoot to make sure key and value are actually invalid.
        # print (state, k, v)
    return state
        
def isValid(filename):
    data = open(filename)
    loadedData = json.load(data)
    valid = 0
    for i in (loadedData):
        if (len(i) == 8) or (len(i) == 7 and 'cid' not in i):
            if handler(i):
                valid += 1
    print (valid)
                                      
if __name__ == "__main__":
    args = sys.argv
    isValid(args[1])