# Author: Sloane Luckiewicz
import turtle 
turtle.bgcolor("sky blue")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.color("black")
pen.hideturtle()
pen.speed(0)
size = 200

# Variables
houseBase = size * .30

# centering
pen.up()
pen.setpos(-houseBase/2, -size/2)
pen.down()
# House 
pen.begin_fill()
pen.fillcolor("orange")
for i in range (4):
    pen.forward(houseBase)
    pen.left(90)
pen.end_fill()

# roof
pen.up()
pen.setpos(-houseBase/1.25, -size/2+houseBase)
pen.down()
pen.begin_fill()
pen.fillcolor("purple")
for i in range (3):
    pen.forward(houseBase+33)
    pen.left(120)
pen.end_fill()

# tree base
pen.up()
pen.setpos(houseBase + 16, -size/2)
pen.down()
pen.begin_fill()
pen.fillcolor("brown")
for i in range (4):
    pen.forward(houseBase/3)
    pen.left(90)
pen.end_fill()

# leaves
pen.up()
pen.setpos(houseBase+27, -size/2 + 14)
pen.down()
pen.begin_fill()
pen.fillcolor("dark green")
pen.circle(houseBase/3.5)
pen.end_fill()

# sun
pen.up()
pen.setpos(-houseBase*2.85, size*.69)
pen.color("yellow")
pen.down()
pen.begin_fill()
pen.fillcolor("yellow")
pen.circle(houseBase/5.5)
pen.end_fill()

# rays
pen.up()
pen.setpos(-houseBase*2.85, size*.75)
pen.color("yellow")
pen.down()
for i in range (12):
    pen.forward(25)
    pen.up()
    pen.setpos(-houseBase*2.85, size*.75)
    pen.down()
    pen.left(30)

turtle.done()