# Author: Sloane Luckiewicz
# Binary / Decimal Conversion Program

# decimal to binary conversion
print("Welcome to Calculator")

def decimalToBinary(dec):
    dec = int(input("Enter decmial to convert to binary: "))
    ans1 = ""

    while dec >0:
        ans1 = str(dec%2) + ans1
        dec = int(dec/2)
    print(ans1)

    while dec < 0:
        print("Invalid. Please enter a positive number.")

# binary to decimal conversion
def binaryToDecimal(binary):
    binary = int(input("Enter binary number to convert to decimal: "))
    ans2 = 0
    i = 0

    while binary >0:
        ans2 += (binary%10)*(2**i)
        i+= 1
        binary= int(binary/10)
    print(ans2)

# calculator
while True:
    userInput = input("Convert from binary to decimal (BTD), decimal to binary (DTB), or (Q)uit: ") .lower() .strip()

    if userInput == 'q':
        print("Goodbye")
        break
    
    elif userInput.upper() == 'DTB':
        decimalToBinary("dec")

    elif userInput.upper() == 'BTD':
        binaryToDecimal("binary")
    
    else:
        print("Invalid comment")

