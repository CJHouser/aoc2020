def readText(filename):
    arr = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in lines:
            arr.append(int(i.rstrip("\n")))
    return (arr)

def calculate():
    array = readText("lines.txt")
    for i in range(len(array)):
        for j in range(1, len(array)):
            for k in range(2, len(array)):
                if (array[i] + array[j] + array[k]) == 2020:
                    return (array[i] * array[j] * array[k])
    
if __name__ == "__main__":
    print (calculate())