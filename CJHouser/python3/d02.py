import boiler

# We can avoid using an if statement because python's booleans can be used
# as integers. Try this in your repl:
# True + True
def part1(inputs):
    result = 0
    for i in inputs:
        lo, hi, c, cs = i
        result += cs.count(c) in range(lo, hi+1)
    return result

# Careful for:
# 1. The passwords are one-indexed, which is why position
#    can be equal to length.
# 2. Using OR instead of XOR. The password should have the character
#    in EXACTLY ONE position.
def part2(inputs):
    result = 0 
    for i in inputs:
        p1, p2, c, cs = i 
        result += (p1 <= p2 <= len(cs) and ((c == cs[p1-1]) ^ (c == cs[p2-1])))
    return result

if __name__ == "__main__":
    contents = boiler.getLines("d02")
    inputs = []
    for i in contents:
        lohi, character, password = i.split(' ')
        lo, hi = lohi.split('-')
        inputs.append([int(lo), int(hi), character[0], password])
    print("Part 1:", part1(inputs))
    print("Part 2:", part2(inputs))
