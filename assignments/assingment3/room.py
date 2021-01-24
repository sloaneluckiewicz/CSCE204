# Author: Sloane Luckiewicz

import math

print("Let's finish your room")

# dimensions
width = float(input("Enter your room width: "))
length = float(input("Enter your room length: "))
height = float(input("Enter your room height: "))

flooring = width * length
ceiling = width * length
drywall = (width * length) + (width * height) + (length * height)

# total cost
totalCost = flooring * 1.5 + ceiling * 0.5 + drywall * 2

print(f"Room finishing cost: ${totalCost}")

