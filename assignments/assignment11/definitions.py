# Author: Sloane Luckiewicz
# File Reading
# Dictionary 

def getDictionary():
    dictionary = {}
    try:
        with open("assignments/assignment11/words.txt") as file:
            for line in file:
                data = line.split(':')
                words = data[0].strip()
                definition = data[1].strip()
                dictionary[words] = definition
            return dictionary
    except FileNotFoundError:
        print("The dictionary file could not be located. Check permissions. ")
        return dictionary

def getDefintion(wordList):
    word = input("Enter a word you want defined: ").strip().lower()
    if word in wordList:
        print(f"{wordList[word]}")
    else:
        print(f"Sorry, {word} is not in my dictionary.")
    
    
def displayDictionary():
    print("Displaying Dictionary")
    wordList = getDictionary()
    for word in wordList:
        print(f"{word}: {wordList[word]}") 

# program 
print("Welcome to my Dictionary")
wordList = getDictionary()

while True:
    command = input("(V)iew, (D)efine, or (Q)uit: ").lower().strip()
    # quit
    if command == "q":
        print("Goodbye")
        break
    # view
    elif command == "v":
        displayDictionary()
    # define
    elif command == "d":
        getDefintion(wordList)