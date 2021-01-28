# Author : Sloane Luckiewicz

import math

#Grade Calculator
print("Calculate Your Grade")

assignments = float(input("Assignments: "))
quizzes = float(input("Quizzes: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))
finalGrade = assignments * 0.40 + quizzes * 0.10 + midterm * 0.25 + final *0.25
letterGrade = "F"

print(f"Your final grade is {round(finalGrade,1)}")

if finalGrade >= 89.5:
    letterGrade = "A"
elif finalGrade >=79.5:
    letterGrade = "B"
elif finalGrade >=69.5:
    letterGrade= "C"
elif finalGrade >=59.5:
    letterGrade= "D"
else:
    letterGrade = "F"

print(f"Letter Grade is {letterGrade}")