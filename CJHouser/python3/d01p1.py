# Create a dictionary where the key and value pairs are complements whose sum
# is 2020.
# i + c = 2020
#     c = 2020 - i
# A complement exists if the complement of a value is a key in the dictionary.
def solution(inputs):
    complements = dict()
    for i in inputs:
        c = complements.setdefault(i, 2020 - i)
        if c in complements:
            return c * complements[c]
    return -1

"""
TODO: tests for practice. make real tests
def tests():
    # empty input has no solution
    t1 = solution([])
    print("empty input", t1)

    # too few input
    t2 = soltuion([10])
    print("too few input", t2)

    # no solution
    t3 = solution([10, 30])
    print("no solution", t3)

    # solution found
    t4 = solution([1000, 1020])
    print("solution 1000 * 1020", t4)

    # identical complements
    t5 = solution([1010, 1010])
    print("solution 1010 * 1010", t5)
        
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
