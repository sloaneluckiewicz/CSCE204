# Author: Sloane Luckiewicz
import turtle 
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("lemonchiffon")

pyramidSize = int(turtle.numinput("Height", "Pyramind Height: ", 5,1,10))
colorList = []

shapeSize = 200/pyramidSize
heightPadding = turtle.window_height()/pyramidSize/3

for i in range(pyramidSize):
    userColor = turtle.textinput("Color", f"Enter desired color for row {i+1}: ") .lower() .strip()
    colorList.append(userColor)

for row in range (pyramidSize):
    x = (-turtle.window_width()*.8)/pyramidSize + row * heightPadding/2
    y = -turtle.window_height()/4 + row * heightPadding

    for col in range (pyramidSize - row):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor(colorList[row])
        pen.begin_fill()
        for i in range (3):
            pen.forward(shapeSize)
            pen.left(120)
        pen.end_fill()
                
        x += heightPadding
         


turtle.done()

