def factorial():
    num = int(input("Enter number: "))
    answer = 1

    # error invalid input   return = takes you out of the function
    if num < 1:
        print("Invalid number")
        return

    for i in range(1, num+1):
        answer *= i

    print(f"{num}! = {answer}")

def power():
    base = int(input("Enter number for base: "))
    exponent = int(input("Enter number for exponent: "))
    answer = 1

    if base < 1 or exponent <1:
        print("invalid input")
        return 

    # loop through and caluculate answer, then display it
    for i in range(exponent):
        answer *= base

    print(f"{base}^{exponent} = {answer}")


def sum():
    number = int(input("Enter number to sum: "))
    ans = 0

    for i in range(1, number+1):
        ans += i
    print(f"The sum of {number} = {ans}")

# program 
print("Welcome to Math!")

while True:
    command = input("Compute (F)actotial, (S)um, (P)ower, or (Q)uit: ").strip() .lower()
    if command == "q":
        break 
    elif command == "f":
        factorial()
    elif command == "s":
        sum()
    elif command == "p":
        power()
    else: 
        print("Invalid input")

print("Goodbye!")


