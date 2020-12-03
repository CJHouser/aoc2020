# Careful for:
# 1. Indexing starts at 1 for the passwords which is why position
#    can be <= length
# 2. Using XOR instead of OR. The password should have the character
#    in EXACTLY ONE position.
def solution(inputs):
    result = 0
    for i in inputs:
        p1, p2, c, cs = i
        result += (p1 <= p2 <= len(cs) and ((c == cs[p1-1]) ^ (c == cs[p2-1])))
    return result

# Boiler plate
def getLines(filename):
    with open("../inputs/" + filename, 'r') as fd:
        lines = fd.readlines()
    return [l.strip() for l in lines]

if __name__ == "__main__":
    contents = getLines("d02")
    inputs = []
    for i in contents:
        entry = i.split(' ')
        lo, hi = entry[0].split('-')
        lo = int(lo)
        hi = int(hi)
        character = entry[1][0]
        password = entry[2]
        inputs.append([lo, hi, character, password])
    print(solution(inputs))
