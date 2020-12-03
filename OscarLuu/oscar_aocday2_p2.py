def readText(filename):
    arr = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in lines:
            arr.append(i.rstrip("\n").replace(":", "").replace("-", " ").split(" "))
    return (arr)

def checkPassword():
    array = readText("puzzle_input/day02.txt")
    results = 0
    for i in array:
        arrayPassword = (list(i[3]))
        positionOne = int(i[0]) - 1
        positionTwo = int(i[1]) - 1
        results += (i[2] == arrayPassword[positionOne]) ^ (i[2] == arrayPassword[positionTwo])

    print (results)            
            
if __name__ == "__main__":
    checkPassword()