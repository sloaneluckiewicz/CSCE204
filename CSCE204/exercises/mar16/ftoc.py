"""
Make a function called fahr_to_cels (fahrenheit) that returns celcius
Make a faunction called cels_to_fahr (celsius) that returns farenheit)
Make a function called miles_to_kilo (miles) that returns kilometers
Make a function called kilo_to_miles (kilo) that returns miles
"""

def fahr_to_cels(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius 

def cels_to_fahr(celsius):
    fahrenheit = celsius * 9/5 +32
    return fahrenheit  

def miles_to_kilos(miles):
    kilos = miles * 1.609344
    return kilos

def kilos_to_miles(kilos):
    miles = kilos * 0.6214
    return miles

print("Conversion Program")
command = int(input(f"""
    Enter Type of Conversion:
    1. Fahrenheit to Celsius
    2. Celsius to Fahrenheit
    3. Miles to Kilometers
    4. Kilometers to Miles
"""))

# invalid command
if command <1 or command > 4:
    print("Invalid command")

# valid command
else:
    value = float(input("Enter Value: "))
    
    if command == 1:
        result = fahr_to_cels(value)
        print(f"{value}F = {result}C")
    elif command ==2:
        result = cels_to_fahr(value)
        print(f"{value}C = {result}F")
    elif command ==3:
        result = miles_to_kilos(value)
        print(f"{value} Miles = {result} Kilo")
    elif command ==4:
        result = kilos_to_miles(value)
        print(f"{value} Kilo = {result} Miles")