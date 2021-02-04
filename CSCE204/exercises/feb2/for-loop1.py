
""" count from 1 to 10
for i in range (1,11): # add another number to desired end
    print(i)
"""

""" loop counting by 2s
for i in range (2,21,2): # last parameter will indicate what you will go by called the STEP
    print(i)
"""

""" loop from 10 to 1
for i in range (10,0,-1): 
    print(i)
"""

"""
# sum the numbers 1 through 10
sum = 0

for i in range (1,11):
    sum += i 

print(f"Sum of numbers 1 through 10: {sum} ")
"""

"""
# sum the numbers 1 through user end
sum = 0
userNum = int(input("Enter number : "))
for i in range(1,userNum + 1):
    sum += i 

print(f"Sum of numbers 1 through {userNum}: {sum} ")
"""

# sum the numbers user start through user end
sum = 0
userStart = int(input("Enter start number: "))
userEnd = int(input("Enter end number: "))
for i in range(userStart,userEnd + 1):
    sum += i 

print(f"Sum of numbers {userStart} through {userEnd}: {sum} ")