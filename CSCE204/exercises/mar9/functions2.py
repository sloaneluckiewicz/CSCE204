import turtle
import random
pen = turtle.Turtle()
turtle.setup(575,575)
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("aliceblue")

# set random variables & position
def set_random_position():
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))

    pen.up()
    pen.setpos(x,y)
    pen.down()

# square function
def draw_square():
    set_random_position()

    length = 50

    for i in range(4):
        pen.forward(length)
        pen.right(90)

# triangle function
def draw_triangle():
    set_random_position()

    length = 50

    for i in range(3):
        pen.forward(length)
        pen.left(120)

# star function
def draw_star():
    set_random_position()

    length= 50

    for i in range(5):
        pen.forward(length)
        pen.right(144)

for i in range(10):
    choice = random.randint(0,2)

    if choice == 0:
        draw_square()
    elif choice == 1:
        draw_triangle()
    elif choice == 2:
        draw_star()


turtle.done()