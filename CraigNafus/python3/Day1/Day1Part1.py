#Problem: find the two entries that sum to 2020 and then multiply those two numbers together.

def main():
    inputList = []
    with open('Day1Input.txt') as openfileobject:
        inputList = openfileobject.read().splitlines()
    
    for i in range(0, len(inputList)):
        for j in range(i+1, len(inputList)):
            if(int(inputList[i]) + int(inputList[j]) == 2020):
                answer = int(inputList[i]) * int(inputList[j])
                print("Numbers that add to 2020 are: " + inputList[i] + " and  " + inputList[j])
                print("Numbers multiplied together: " + str(answer))
        
if __name__ == "__main__":
    main()