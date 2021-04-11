# Author: Sloane Luckiewicz
# OOP 

from bird import Bird

bird_list = (
    Bird("Penguin", "Black & White", "krill, fish, and squid", "Flightless birds with a big head, short neck, and elongated body that live in Antarctica"),
    Bird("Flamingo", "Pink", "blue-green and red algae, diatoms, and insects", "Bird with long neck and sticklight legs with pink feathers"),
    Bird("Ostrich", "Black, white, and light brown", "roots, flowers, fruits, and small insects and lizards", "Large, flighless birds that run up to 43 mph"),
    Bird("Hummingbird", "purple, green, yellow, red", "bugs and nectar", "Small birds between 3-5 inches in length, with a long beak to extract nectar")
)

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