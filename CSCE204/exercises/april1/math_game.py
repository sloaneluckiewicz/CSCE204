import random 

def get_score():
    with open("exercises/april1/score.txt") as file:
        for line in file:
            return int(line)

        return 0 

# save score to file 
def save_score(score):
    with open ("exercises/april1/score.txt", "w") as file:
        file.write(f"{score}")
        
def play_round():
    randNum = random.randint(1000,9999)
    sum = sum_digits(randNum)

    userAnswer = int(input(f"Sum digits in {randNum}: "))

    if userAnswer == sum:
        return True
    else:
        print(f"Sorry, the number should be {sum}.")
        return False


def sum_digits(num):
    sum = 0 

    while num > 0:
        digit = num % 10 
        sum += digit 
        num = num // 10

    return sum


score = get_score()

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break 
    if command != "p":
        print("Invalid command")
        continue 
    
    if play_round():
        score += 1
        print("YAY!")
        

print("Goodbye")
save_score(score)
print(f"Your current score is {score}")