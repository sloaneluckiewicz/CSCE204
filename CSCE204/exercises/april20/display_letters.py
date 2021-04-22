def display_letters(word):
    for i in range(len(word)):
        print(word[i])

def display_star_word(word):
    print("*", end="")

    for letter in word:
        print(letter + "*", end="")

    print()

def in_word(word,letter):
    for let in word:
        if let == letter:
            return True

    return False

display_letters("Jimmy")

display_star_word("everything")

if in_word("star", "f"):
    print("YAY")
else:
    print("NAY!")