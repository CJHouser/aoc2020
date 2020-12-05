import boiler

# The modulo operator can be used for wrap indexing
def part1(inputs, vector):
    width = len(inputs[0])
    trees = 0
    x = 0
    y = 0
    while y < len(inputs):
        trees += '#' == inputs[y][x % width]
        x += vector[0]
        y += vector[1]
    return trees

# The accumulator starts at one because of the multiplicative identity of
# integers:
# a * 1 = a
def part2(inputs, vectors):
    result = 1
    for v in vectors:
        result *= part1(inputs, v)
    return result

if __name__ == "__main__":
    inputs = boiler.getLines("d03")
    print("Part 1:", part1(inputs, (3, 1)))
    vectors = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print("Part 2:", part2(inputs, vectors))
