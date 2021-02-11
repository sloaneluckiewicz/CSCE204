# merging grades and loop validation
numGrades = int(input("Enter number of grades: "))
sum = 0

# loop and gather grades
# float is decimal and int is whole number
for i in range (numGrades):
    grade = float(input(f"Enter Grade {i+1}: "))

    while grade < 0 or grade > 100:
        print("Invalid grade, please enter a number in the range: 1-100 ")
        grade = float(input(f"Enter Grade {i+1}: "))
    
    sum += grade 

average = sum / numGrades
print(f"Your average is {average}")