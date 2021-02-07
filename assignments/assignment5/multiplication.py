# Author: Sloane Luckiewicz

import random 

# generate a random number between 1-100

print("Welcome to our multiplication game")

userInput = input("Shall we ask you a question (Y)es or (N)o: ") .strip().lower()

while userInput == "y":
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    userGuess = input(str(num1) + "*" + str(num2) + "=" )
    answer = str(num1 * num2)
    if userGuess == answer:
        print("Correct!")
        userInput = input("Shall we ask you a question (Y)es or (N)o: ") .strip().lower()
    else:
        print(f"Incorrect. The answer is {answer}")
        userInput = input("Shall we ask you a question (Y)es or (N)o: ") .strip().lower()
print("Goodbye!")