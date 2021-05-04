# Author: Sloane Luckiewicz
# Final - Hangman
from hangman import Man 

import turtle
import random 
turtle.bgcolor("navajo white")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(10)
pen.pensize(2)
pen.hideturtle()
style = ("Courier", 20)

def begin():
    word_options = []
    with open ("assignments/final/words.txt") as file:
        for line in file:
            word_option = line.replace("\n", "").strip().lower()
            word_options.append(word_option)
        return word_options

def random_choice(options):
    the_word = random.choice(options)
    print(f"{the_word}")
    return the_word

def create_hyphen(word):
    hyphen_word = ""
    for i in range(len(word)):
        hyphen_word += "_"
    return hyphen_word

def display_word(word):
    display_word = " "
    pen.penup()
    pen.setpos(-150,175)
    pen.pendown()
    for i in range(len(word)):
        display_word += word[i] + " "
    pen.write(display_word, font = style)

def check_word(word, letter):
    for i in word:
        if i.lower() == letter.lower():
            return True
    return False

def guess_letter(x,y):
    import turtle
    global the_word_chosen
    global guessed_word
    global wrong_attempt_number
    new_guessed_word = ""
    wrong_possibility = 0
    outcome = 0
    guessed_word = create_hyphen(the_word_chosen)
    letter = turtle.textinput("Guess Letter", "Guess a letter: ")
    
    for i in range(len(the_word_chosen)):
        if the_word_chosen[i] == letter:
            new_guessed_word += letter
        else:
            new_guessed_word += guessed_word[i]

    for i in range(len(the_word_chosen)):
        if the_word_chosen[i] != letter:
            wrong_possibility += 1
        else:
            continue

    if wrong_possibility == len(the_word_chosen):
        wrong_attempt_number += 1
    guessed_word = new_guessed_word
    man = Man(50, wrong_attempt_number, outcome)
    if new_guessed_word == the_word_chosen:
        outcome += 1
        man.write_winner(pen)
    display_word(guessed_word)

    man = Man(50, wrong_attempt_number, outcome)
    man.draw(pen)

options = begin()
the_word_chosen = random_choice(options)
guessed_word = create_hyphen(the_word_chosen)
display_word(guessed_word)
x = 0
y = 0
wrong_attempt_number = 0

turtle.onscreenclick(guess_letter)

turtle.done()