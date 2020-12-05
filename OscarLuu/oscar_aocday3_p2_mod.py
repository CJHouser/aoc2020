def readText(filename):
    arr = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in lines:
            arr.append(list(i.rstrip('\n')))
    return (arr)

def treeCounter(coords):
    array = readText("puzzle_input/day03.txt")
    trees = 0
    column = coords[0]
    row = coords[1]
    while row < len(array):
        column = column % len(array[0])
        print (row, column)
        if array[row][column] == "#":
            trees += 1
        column += coords[0]
        row += coords[1]
    return (trees)

def addRowColumn():
    coords = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    multiplyTrees = 1
    for i in coords:
        multiplyTrees *= treeCounter(i)
    return (multiplyTrees)    
if __name__ == "__main__":
    print (addRowColumn())
    