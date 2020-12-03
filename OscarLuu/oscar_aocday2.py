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
        counter = i[3].count(i[2])
        if counter in range(int(i[0]), int(i[1]) + 1):
            results += 1
    print (results)
            
if __name__ == "__main__":
    checkPassword()