while True:
    try:
        number = int(input("Enter number: "))
        break
    except ValueError:
        print("Sorry you did not enter a valid whole number")
