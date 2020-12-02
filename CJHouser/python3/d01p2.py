# Rerun the solution to part 1 for each input in the list
# i + j + c = 2020
#     j + c = 2020 - i
# (2020 - a) becomes the target instead of 2020 alone. This reduces the
# problem to:
#     j + c = target
# which is just problem 1 in a different form:
#     i + c = 2020
def solution(inputs):
    for i in range(len(inputs) - 1):
        target = 2020 - inputs[i]
        complements = dict()
        for j in range(i + 1, len(inputs)):
            c = complements.setdefault(inputs[j], target - inputs[j])
            if c in complements:
                return c * inputs[j] * inputs[i]
    return -1

"""
Attempt #1
def solution(inputs):
    complements = dict()
    for i in range(len(inputs) - 1):
        for j in range(i + 1, len(inputs)):
            partial_sum = inputs[i] + inputs[j]
            c = complements.setdefault(partial_sum, 2020 - partial_sum)
            if c in complements:
                return c * inputs[i] * inputs[j]
    return None
"""

"""
write some tests
"""

# Boiler plate
def getLines(filename):
    with open("../inputs/" + filename, 'r') as fd:
        lines = fd.readlines()
    return [l.strip() for l in lines]

if __name__ == "__main__":
    inputs = getLines("d01")
    inputs = [int(i) for i in inputs]
    print(solution(inputs))
