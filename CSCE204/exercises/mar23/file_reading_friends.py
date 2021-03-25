"""
with open("exercises/mar23/friends.txt") as file:
    for line in file:
        print(line, end="")
"""

# create an array of friends from file
def get_friends():
    friends = []

    # populate array with friends from file
    with open("exercises/mar23/friends.txt") as file:
        for line in file:
            friend = line.replace("\n", "")
            friends.append(friend)

    return friends


# get friends, loop through and display them 
chums = get_friends()

print("My Besties for the Resties: ")

# loop through and display list of friend in format: 1. amy
for i in range(len(chums)):
    print(f"{i+1}. {chums[i]}")