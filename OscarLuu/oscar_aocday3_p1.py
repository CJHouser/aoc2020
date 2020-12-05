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
    right = 0
    for i in range(len(array)):
        try:
            if array[i][right] == "#":
                trees += 1
        except IndexError:
            right = right - len(array[0])
            if array[i][right] == "#":
                trees += 1
        right += 3

    print (trees)
    
    
if __name__ == "__main__":
    treeCounter()