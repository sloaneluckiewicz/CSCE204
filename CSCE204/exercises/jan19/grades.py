# Author : Sloane Luckiewicz

import math

#Grade Calculator
print("Grade Calculator")

assignments = float(input("Enter Assignments: "))
exercises = float(input("Enter Exercises: "))
quizzes = float(input("Enter Quizzes: "))
midterm = float(input("Enter Midterm: "))
final = float(input("Enter Final: "))
finalGrade = assignments * 0.25 + exercises * 0.10 + quizzes * 0.15 + midterm * 0.25 + final *0.25
finalGrade = round(finalGrade, 1)
 

print(f"Your final grade is {finalGrade}.")