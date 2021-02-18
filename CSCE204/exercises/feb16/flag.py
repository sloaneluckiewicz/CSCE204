import turtle
import random
turtle.setup(575,575)
pen= turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

# draw rectangle
pen.up()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.down()

pen.color("blue")
pen.begin_fill()
for i in range (4):
    if i % 2 == 0:  # RECTANGLE ! if i is even, divided by 2 has no remainder
        pen.forward(turtle.window_width()/2)
    else:
        pen.forward(turtle.window_height())
    pen.left(90)
pen.end_fill()

# stripes
pen.color("red")
stripeHeight = turtle.window_height()/13
stripeWidth = turtle.window_width()/2

for i in range (0, 13, 2):  #start, end, jump by
    pen.up()
    y = -turtle.window_height()/2 + stripeHeight * i
    pen.setpos(0, int(y))
    pen.down()
    
    # draw red band
    pen.begin_fill()
    for j in range (4):
        if j % 2 == 0: #if even
            pen.forward(stripeWidth)
        else:
            pen.forward(stripeHeight)
        pen.left(90)
    pen.end_fill() 

# draw star
starWidth = 20
for i in range(50):
    x = random.randint(-int(turtle.window_width()/2), -starWidth)
    y = random.randint(-int(turtle.window_height()/2) + starWidth, int(turtle.window_height()/2- starWidth))
    
    pen.up()
    pen.setpos(x,y)
    pen.down()

    pen.color("white")
    # draw a star
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x,y+starWidth/2)
    pen.down()
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()

turtle.done()