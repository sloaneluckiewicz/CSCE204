# Author: Sloane Luckiewicz

import turtle
turtle.bgcolor("navajowhite")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

# set up
shapeList = []
shapeNum = int(turtle.numinput("Shapes", "Enter how many shapes you want to draw: ", 5, 1, 10))
shapeSize = 50

# enter number of shapes
for i in range(shapeNum):
    userShape = turtle.textinput("Shapes", "Enter desired shape (circle, square, triangle, star, or diamond): ") .lower() .strip()
    shapeList.append(userShape)

# drawing the shape
for shape in shapeList:
    pen.up()
    pen.setpos(-125,0)
    pen.down()

    if shape == "circle":
        pen.circle(shapeSize/2)
    elif shape == "square":
        pen.up()
        pen.setpos(-80,0)
        pen.down()
        for i in range(4):
            pen.forward(shapeSize)
            pen.left(90)
    elif shape == "triangle":
        pen.up()
        pen.setpos(-10,0)
        pen.down()
        for i in range (3):
            pen.forward(shapeSize)
            pen.left(120)
    elif shape == "star":
        pen.up()
        pen.setpos(50,10)
        pen.down()
        for i in range (3):
            pen.forward(shapeSize)
            pen.left(120)
        pen.up()
        pen.sety(35)
        pen.down()
        for i in range (3):
            pen.forward(shapeSize)
            pen.right(120)
turtle.done()