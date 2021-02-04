userInput = input("Do you want to say hello (Y or N): ") .strip().lower()

while userInput == "y":
    print("Hello")
    userInput = input("Do you want to say hello again? ") .lower() .strip()

print("Goodbye")