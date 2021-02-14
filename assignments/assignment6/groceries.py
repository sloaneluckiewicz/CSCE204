# Author: Sloane Luckiewicz

print("Welcome to our grocery store ")

groceryItems = ["pomegranate seeds", "apple juice", "buffalo chicken dip", "dark chocolate", "potato"]

# display all items in list
print("The following items are in our grocery store:")
for grocery in groceryItems:
    print(grocery)

# user input
order = input("What would you like to buy? ") .lower() .strip()

if order in groceryItems:
    print(f"We've ordered {order} for you")
    groceryItems.remove(order)
    print("Now the grocery store contains: ")
    for grocery in groceryItems:
        print(grocery)
else:
    print(f"Sorry we don't have any {order}")
    print("The following items are in our grocery store: ")
    for grocery in groceryItems:
        print(grocery)


print("Thank you. Goodbye")

