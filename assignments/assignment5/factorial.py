# Author: Sloane Luckiewicz

print("Welcome to our factorial generator")

# factorial 
factorial = 1
userNum = int(input("Enter number: "))
for i in range(1,userNum +1):
    factorial = i * factorial 

# finish
print(f"The factorial of {userNum} is {factorial} ")