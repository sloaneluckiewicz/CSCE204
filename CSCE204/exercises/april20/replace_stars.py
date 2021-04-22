def replace_stars(word):
    answer = ""

    for letter in word:
        if letter == "*":
            answer += "."
        else:
            answer += letter

    word = answer
    return answer

word = "a*b*c*d*"
answer = replace_stars(word)
print(word)

"""
def replace_stars(word):
    answer = ""
    global word

    for letter in word:
        if letter == "*":
                answer += "."
        else:
            answer += letter

    word = answer

word = "a*b*c*d*"
replace_stars()
print(word)
"""