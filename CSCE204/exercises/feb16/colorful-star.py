import turtle
import random
turtle.setup(575,575)
pen= turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

colors = ("lavenderblush", "lightpink", "mediumspringgreen", "mistyrose", "yellow", "firebrick", "steelblue", "thistle", "lightcyan")

# draw 100 stars
for i in range (100):
    starWidth = random.randint(20,80)
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))
    color= random.choice(colors)
    pen.color(color)

    # set the position
    # then draw a line of star width
    pen.up()
    pen.setpos(x,y)
    pen.down()

    # top of triangle
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()

    # bottom of triange
    pen.up()
    pen.setpos(x,y+starWidth/2)
    pen.down()
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()


turtle.done()