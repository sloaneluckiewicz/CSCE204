# Author: Sloane Luckiewicz
# Get grades from a user (how many they want)
# Sum them and calculate the average

print("Grade Program")
numGrades = int(input("How many grades: "))
gradeTotal = 0

# Loop through 
for i in range (1, numGrades+1): 
    gradeTotal += int(input(f"Enter Grade {i} "))

average = gradeTotal/numGrades
print(f"Your Average is {round(average,1)}")

