import random 

# generate a random number between 1-100
goal = random.randint(1,100)

print(f"Number to guess is {goal}")

guess = int(input("Enter a number between 1 and 100 "))

# while they have not guessed the correct number
# != means not equal to
while guess != goal:
    # give feedback and get a new guess
    print("WRONG! ")

    if guess < goal:
        print("Too low ")
    elif guess > goal:
        print("Too high ")
        
    guess = int(input("Guess again! "))
   
print("Congrats! You got it right! ")