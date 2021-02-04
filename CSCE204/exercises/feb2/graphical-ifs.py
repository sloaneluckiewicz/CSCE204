# Author: Sloane Luckiewicz
# Create shapes based on user input

import turtle
turtle.bgcolor("light pink")
pen = turtle.Turtle()
pen.pensize(2)

# Ask the user for the shape they want to draw
shape = turtle.textinput("Shapes" , "Enter Shape: ").lower().strip()
shapeSize = 200

# Ask user for a color then set the fill color
color = turtle.textinput("Color" , "Enter Color: ").lower().strip()

# Ask user for a size between 1 and 10, and adjust
shapeSize = turtle.numinput("Size", "Enter Size: ", 5,1,10)*100

pen.fillcolor(color)

if shape == "circle": 
    pen.up()
    pen.setpos(0,-shapeSize/2)
    pen.down()
    pen.begin_fill()
    pen.circle(shapeSize/2)
    pen.end_fill()

elif shape == "square":
    pen.up()
    pen.setpos(-shapeSize/2, -shapeSize/2)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        pen.forward(shapeSize)
        pen.left(90)
    pen.end_fill()

elif shape == "triangle":
    pen.up()
    pen.setpos(-shapeSize/2,-shapeSize/2)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(shapeSize)
        pen.left(120)
    pen.end_fill()

turtle.done()