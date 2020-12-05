import boiler
import re

def part1(fs, ps, part1):
    valid_count = 0
    for p in ps:
        valid = True
        i = 0
        while i < len(fs) and valid:
            if fs[i] not in p and fs[i] != "cid":
                valid = False
            i += 1
        valid_count += valid and (part1 or validate(p))
    return valid_count

def validate(p):
    v = True
    i = 0
    keys = list(p.keys())
    while i < len(keys) and v:
        if keys[i] != "cid":
            v = dispatch[keys[i]](p[keys[i]])
        i += 1
    return v

def checkHeight(n):
    v = True
    height = re.match("^[0-9]+[cm$|in$]", n)
    if not height:
        v = False
    else:
        if n[-2:] == "cm" and int(n[:-2]) not in range(150, 194):
            v = False
        if n[-2:] == "in" and int(n[:-2]) not in range(59, 77):
            v = False
    return v

dispatch = {
    "byr": (lambda n: int(n) in range(1920, 2003)),
    "iyr": (lambda n: int(n) in range(2010, 2021)),
    "eyr": (lambda n: int(n) in range(2020, 2031)),
    "hgt": checkHeight,
    "hcl": (lambda n: re.match("^#[0-9a-f]{6}$", n) != None),
    "ecl": (lambda n: n in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": (lambda n: re.match("^[0-9]{9}$", n) != None),
}

if __name__ == "__main__":
    entries = boiler.fileContents("d04").split("\n\n")
    passports = []
    for e in entries:
        e_fields = re.findall("[a-zA-Z]+:#*[a-zA-Z0-9]*(?=[\s\n]*)", e)
        passport = dict()
        for ef in e_fields:
            key, value = ef.split(':')
            passport[key] = value
        passports.append(passport)
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    print(part1(fields, passports, True))
    print(part1(fields, passports, False))
