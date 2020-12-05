import boiler

# Create a dictionary where the key and value pairs are complements whose sum
# is 2020.
# i + c = 2020
#     c = 2020 - i
# A solution exists if the complement of an input already a key in the
# dictionary.
def part1(inputs):
    complements = dict()
    for i in inputs:
        c = complements.setdefault(i, 2020 - i)
        if c in complements:
            return c * complements[c]

# Rerun part 1 for each input in the list
# j + i + c = 2020
#     i + c = 2020 - j
# (2020 - j) becomes the new target, reducing the problem to problem 1:
#     i + c = target
def part2(inputs):
    for i in range(len(inputs) - 1):
        target = 2020 - inputs[i]
        complements = dict()
        for j in range(i + 1, len(inputs)):
            c = complements.setdefault(inputs[j], target - inputs[j])
            if c in complements:
                return c * inputs[j] * inputs[i]

if __name__ == "__main__":
    inputs = boiler.getLines("d01")
    inputs = [int(i) for i in inputs]
    print("Part 1:", part1(inputs))
    print("Part 2:", part2(inputs))
