class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, correct_answer):
        self.prompt = prompt 
        self.correct_answer = correct_answer
        self.answers = (answer1, answer2, answer3, answer4)

    # loop through answers and display them like: 1. 
    def display_answers(self):
        for i in range(len(self.answers)):
            print(f"{i+1}. {self.answers[i]}") 

