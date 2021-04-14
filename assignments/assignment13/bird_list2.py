# Author: Sloane Luckiewicz
# OOP Part 2
from birds2 import Bird 

def get_birds():
    bird_list = []

    with open("assignments/assignment13/birds.txt") as file:
        for line in file:
            data = line.split(':')
            bird_type = data[0].strip()
            color = data[1].strip()
            food = data[2].strip()
            description = data[3].strip()
            bird_list.append(Bird(bird_type, color, food, description))
    
        return bird_list

bird_list = get_birds()

print("Bird Program!")
while True:
    command = input("(L)ist all birds, get a bird's (D)etails, or (Q)uit: ").strip().lower()
    
    if command == "q":
        break

    elif command == "l":
        for bird in bird_list:
            bird.display()

    elif command == "d":
        bird_name = input("Enter bird name you want identified: ").strip()
        for bird in bird_list:
            if bird.is_match(bird_name):
                bird.display()
    
    else:
        print("Invalid command.")

print("Goodbye!")