friends = ["Jane", "Camille", "Lena", "Steph", "Mike", "Dylan", "Sean", "Jaylen", "Kaden", "Remi"]

# w overwrites 
# a appends

with open("exercises/april1/friends.txt", "w") as file:
    for friend in friends:
        file.write(f"{friend}\n")