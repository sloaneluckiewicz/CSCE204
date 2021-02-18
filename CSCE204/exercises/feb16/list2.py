toys = ["truck", "crayons", "train", "teddy bear", "ball"]

print("Welcome to our toy store!")

# FOR = definitive ending number WHILE = nondefinitive -loop until i say stop
while True:
    command = input("(L)ist, (A)dd, (R)emove, or (Q)uit: ").lower().strip()

    if command == "q":
        break
    elif command == "l":
        for i in range(len(toys)):
            print(f"{i+1}. {toys[i]}")
    elif command == "a":
        toy = input("Enter toy: ").lower().strip()

        if(toy != "" and (toy in toys) == False):
            toys.append(toy)
        else:
            print("Invalid toy name, either empty or already in the list")
    elif command == "r":
        toy = input("Enter toy: ") .lower() .strip()
        if toy in toys:
            toys.remove(toy)
    else:
        print("Invalid input, try again.")


print("Goodbye!")