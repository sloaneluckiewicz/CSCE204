# Author: Sloane Luckiewicz
# File Writing Assignment --> ex. book_list.py

FILE_NAME = "assignments/assignment12/bands.txt"

def writeBands(bands):
    with open(FILE_NAME, "w") as file:
        for band in bands:
            file.write(band + "\n")

def readBands():
    bands = []
    with open(FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","").strip()
            bands.append(line)
    return bands

def listBands(bands):
    for i in range(len(bands)):
        print(f"{i+1}. {bands[i]}")

def addBand(bands):
    band = input("Enter band/artist you want added: ").strip()
    bands.append(band)
    writeBands(bands)
    print(f"{band} was added. ")
    return bands

def deleteBand(bands):
    index = input("Enter band/artist name you want deleted: ").strip().lower()
    if index in bands:
        band = bands.remove(index)
        writeBands(bands)
        print(f"{index} was deleted. ")
    else:
        print("Sorry, invalid band/artist")
        
    return bands

while True: 
    command = input("Enter (L)ist, (A)dd, (D)elete, (Q)uit: ").lower().strip()
    bands = readBands()

    if command == "l":
        listBands(bands)
    
    elif command =="a":
        bands = addBand(bands)
    
    elif command == "d":
        bands = deleteBand(bands)
    
    elif command == "q":
        break 

    else:
        print("Invalid command, try again.")

print("Goodbye!")