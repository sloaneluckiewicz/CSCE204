print("What should you Wear?: ")

temp = float(input("Enter Temperature: "))
precip = input("Enter Precipiatation (R)ain, (S)now, (N)one: ") .lower() .strip()

if temp <= 32 and precip == "n":
    print("Wear a warm jacket")
if temp <= 32 and precip == "s":
    print("Wear a snowsuit")
if temp <= 50 and precip == "n":
    print("Wear a jacket")
if temp <= 50 and precip == "r":
    print("Wear a rain jacket")
else:
    print("Sorry this app is not complete")