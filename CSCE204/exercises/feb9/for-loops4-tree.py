# Author: Sloane Luckiewicz

import turtle 
turtle.bgcolor("navy")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.color("white")
pen.fillcolor("green")
pen.hideturtle()
pen.speed(0)
size = 200

# all relative to size = 200
smSize = size * .15
mdSize = size * .3
lgSize = size * .4
trunkSize = size * .15

# set initial position to center
pen.up()
pen.setpos(-trunkSize/2, -size/2)
pen.down()

# trunk 
pen.begin_fill()
pen.fillcolor("brown")
for i in range (4):
    pen.forward(trunkSize)
    pen.left(90)
pen.end_fill()

# big tree
pen.up()
pen.setpos(mdSize/1.5 - lgSize, -size/2 + trunkSize)
pen.down()
pen.begin_fill()
pen.fillcolor("green")
for i in range (3):
    pen.forward(lgSize)
    pen.left(120)
pen.end_fill()

# md tree
pen.up()
pen.setpos(-mdSize/2, -lgSize + mdSize)
pen.down()
pen.begin_fill()
pen.fillcolor("green")
for i in range (3):
    pen.forward(mdSize)
    pen.left(120)
pen.end_fill()

# sm tree
pen.up()
pen.setpos(-mdSize + smSize*1.5, mdSize/2.5)
pen.down()
pen.begin_fill()
pen.fillcolor("green")
for i in range (3):
    pen.forward(smSize)
    pen.left(120)
pen.end_fill()

turtle.done()