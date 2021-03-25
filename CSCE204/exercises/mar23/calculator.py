# ask the user to enter a price, if they enter a valid float return it 
# if they enter an invalid float, give them feedback and keep looping

def getPrice():
   while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Sorry, you did not enter a valid number")

# ask the user to enter a quantity, if they enter a valid int, return in 
# if they enter an invalid int, give them feedback and keep looping 

def getQuantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Sorry, you did not enter a valid number")

# calculator program 
print("Our cost calculator")
price = getPrice()
quantity = getQuantity()
total = quantity*price*1.07
print(F"Your total is ${round(total,2)}.")