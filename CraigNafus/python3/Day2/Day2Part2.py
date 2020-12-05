# Problem: find the count of valid passwords. first position must contain the letter, and the second must not bet the letter.
# ex: 1-4 a : abcwer  <--- password is valid, first letter is a, and 4th is not.

def main():
    inputList = []
    with open('Day2Input.txt') as openfileobject:
        validPasswordCount = 0
        for line in openfileobject:
            firstNum = line.split('-')[0]
            secondNum = line[(len(firstNum) + 1):].split(' ')[0]
            letterToSearchFor = line[(len(firstNum) + 1 + len(secondNum) + 1):].split(':')[0]
            password = line.rsplit(':')[1].strip(' ').strip('\n')
            
            firstNumIndex = int(firstNum) - 1
            secondNumIndex = int(secondNum) - 1

            if((password[firstNumIndex] == letterToSearchFor) and (password[secondNumIndex] != letterToSearchFor)):
                validPasswordCount+=1
            elif((password[firstNumIndex] != letterToSearchFor) and (password[secondNumIndex] == letterToSearchFor)):
                validPasswordCount+=1

    print("Total number of valid passwords: " + str(validPasswordCount))
        
if __name__ == "__main__":
    main()
