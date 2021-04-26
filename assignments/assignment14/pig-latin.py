# Author: Sloane Luckiewicz 
# String Manipulation

def is_vowel(letter):
    let = letter[0]
    if let.lower() == "a" or let.lower()  == "e" or let.lower()  == "i" or let.lower() == "o" or  let.lower() == "u":
        return True
    else:
        return False


def convert_to_pig_latin(word):
    if is_vowel(word):
        print(f"{word} in Pig-Latin is: {word}-hay.")
    else:
        pig_latin = word[0]
        answer = ""

        for i in word:
            if i == word[0]:
                continue
            else:
                answer += i
        
        print(f"{word} in Pig-Latin is: {answer}-{pig_latin}.")


print("Welcome to Our Pig-Latin Translator :) ")
while True:
    command = input("(C)onvert or (Q)uit?: ").lower().strip()
    if command == "q":
        break
    elif command == "c":
        word = input("Enter a word: ")
        answer = convert_to_pig_latin(word)
    else:
        print("INVALID COMMAND")


print("Goodbye")