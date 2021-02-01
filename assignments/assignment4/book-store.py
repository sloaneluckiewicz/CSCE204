# Author: Sloane Luckiewicz

print("Welcome to our bookstore")
action = input("What would you like to do (V)iew or (O)rder: ") .lower() .strip() 

# View
if action == "v":
    print("""Our catalogue consists of: 
    1984 by George Orwell
    The Help by Kathryn Stockett
    Gone with the Wind by Margaret Mitchell
    The fellowship of the Ring by J.R.R. Tolkien""")

# Order
elif action == "o":
    bookName = input("Enter book name: ") .lower() .strip()
    if bookName == "1984":
        print("You can buy 1984 for $9.99")
    elif bookName == "the help":
        print("You can buy The Help for $7.59")
    elif bookName == "gone with the wind":
        print("You can buy Gone with the Wind for $8.50")
    elif bookName == "the fellowship":
        print("You can buy The Fellowship for $10.11")

print("Have a nice day")
