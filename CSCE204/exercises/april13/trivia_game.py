from question import Question
import random 

question1= Question("What type of animal is a seahorse?", "Crustacean", "Arachnid", "Fish", "Shell", 2)

questions = (
    Question("question 1 prompt", "q1 a1", "q1 a2", "q1 a3", "q1 a4", 0),
    Question("question 2 prompt", "q2 a1", "q2 a2", "q2 a3", "q2 a4", 1),
    Question("question 3 prompt", "q3 a1", "q3 a2", "q3 a3", "q3 a4", 2),
    Question("question 4 prompt", "q4 a1", "q4 a2", "q4 a3", "q4 a4", 3)
)

print("Trivia Game")

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        break
    elif command != "p":
        print("Invalid input")
        continue 
    
    question = random.choice(questions)
    print(question.prompt)
    question.display_answers()
    user_ans = int(input("Enter numerical answer: "))

    if question.correct_answer == user_ans - 1:
        print("NICE!")
    else:
        print("WRONG!")

print("Goodbye!")
