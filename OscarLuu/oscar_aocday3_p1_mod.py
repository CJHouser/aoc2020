def readText(filename):
    arr = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in lines:
            arr.append(list(i.rstrip('\n')))
    return (arr)

def treeCounter():
    array = readText("puzzle_input/day03.txt")
    trees = 0
    index = 0
    for i in range(len(array)):
        index = index % len(array)
        if array[i][index] == "#":
            trees += 1

    print (trees)
    
    
if __name__ == "__main__":
    treeCounter()