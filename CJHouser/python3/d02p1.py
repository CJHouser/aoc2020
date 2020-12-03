# We can avoid using an if statement because python's booleans can be used
# as integers.
# Try this in your repl:
# True + True
# it should produce 2
def solution(inputs):
    result = 0
    for i in inputs:
        lo, hi, c, cs = i
        result += cs.count(c) in range(lo, hi+1)
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
