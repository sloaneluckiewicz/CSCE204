# Practicing with the Math Operations
# Author: Sloane Luckiewicz

import math 

# Age predictor 
age = float(input("Enter age: "))
decade = 10
futureAge = age + decade 

print(f"""You are {age} years old.
In a decade you will be {futureAge}""")

# / float division, will be precise and result in a decimal 
# // integer division, will cut off the decimal 
# round (variable, decimal places) ... round(3.75,1) = 3.8
# Pizza Party
numGuests = int(input("Enter Num Guests: "))
slicesPerGuest = 2.5
totalSlices = numGuests * slicesPerGuest
numPizzas = totalSlices // 6
# numPizzas = math.ceil(numPizzas)
numPizzas = round(numPizzas,0)
# math.ceil is not working for me!

print(f"""You are having {numGuests} people to your party.
You will need {totalSlices} number of pizza slices, 
and {numPizzas} pizzas.""")

# chickens
numEggs = 57
numCartons = numEggs // 12

print(f"You need {numCartons} cartons of eggs.")

# travelling 
miles = float(input("Enter Miles: "))
pricePerMile = float(input("Enter Price Per Mile: "))
totalCost = round(miles * pricePerMile,2)

print(f"You will be charged ${totalCost}")
