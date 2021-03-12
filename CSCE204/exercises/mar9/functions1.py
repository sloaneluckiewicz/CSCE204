# function give name and you can call on it whenever you want

def say_hello(firstName, lastName):       # equivalent to firstName = sloane
    print(f"Hola {firstName} {lastName}")
    print("Que tenga un buen día!")

def say_goodbye(firstName, lastName):
    print(f"Adios {firstName} {lastName}!")

print("My Simple Program")
userFirstName = input("Enter first name: ")
userLastName = input("Enter last name: ")
say_hello(userFirstName, userLastName)
say_goodbye(userFirstName, userLastName)
    

