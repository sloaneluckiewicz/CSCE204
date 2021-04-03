import random
FILE_NAME_TRIVIA = "assignments/assignment12/trivia.txt"
 
# Reach each line of the file into a dictionary.  The dictionary will look like:
# Question -> Answer 
# We use a convert to bool method to convert "true" to True  
def getQuestions():
    questions = {}
    with open(FILE_NAME_TRIVIA) as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions[question] = convertToBool(answer)
        return questions

# Converts a string representation of a boolean to a Boolean
def convertToBool(answer):
    if answer == "true":
        return True
    else:
        return False

# Asks the user a random trivia question
# Gathers the users answer
# if their answer is the stored answer then return true (they won), otherwise return false
def getScores():
    scores = []
    with open("assignments/assignment12/score.txt") as file:
        for line in file:
            scores.append(int(line))
        return scores
    
def saveScores(scores):
    with open("assignments/assignment12/score.txt","w") as file:
        file.write(f"{scores[0]}/n")
        file.write(f"{scores[1]}/n")
        file.write(f"{scores[2]}/n")

def playRound():
    question = random.choice(list(questions.keys()))
    userAns = input(f"True or False: {question} ").strip().lower()
    compAns = questions.get(question)

    if convertToBool(userAns) == compAns:
        return True
    else:
        return False

# Let's play the game
print("Welcome to our Trivia Game")

# Load all the questions from the file
questions = getQuestions()

# Loop as long as the user wants to keep playing
scores = getScores()
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    # if they enter q, quit the game
    if command == "q":
        break
    # if they enter an invalid command, indicate that
    elif command != "p":
        print("Invalid command")
        continue
    
    # otherwise play around, if playRound is true, they won
    if playRound():
        scores[1] += 1
        print("Yay, you got it!")
    else:
        scores[2] +=1
        print("Sorry, incorrect")
    scores[0] +=1

saveScores(scores)
print(f"Games played: " + str(scores[0]))
print(f"Games won: " + str(scores[1]))
print(f"Games lost: " + str(scores[2]))
print("Goodbye")