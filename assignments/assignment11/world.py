# Author: Sloane Luckiewicz
import turtle 
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("midnightblue")

def getScene():
    sceneShape = []
    try:
        with open("assignments/assignment11/scene.txt") as file:
            for line in file:
                scene = line.replace("\n", " ").strip().lower()
                sceneShape.append(scene)
    except FileNotFoundError:
        print("Sorry invalid file")

    return sceneShape

def drawTriangle(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    for i in range (3):
        pen.forward(size)
        pen.left(120)
    pen.setheading(0)

def drawUpsideDownTriangle(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    for i in range(3):
        pen.forward(size)
        pen.left(240)
    pen.setheading(0)

def drawStar(x,width):
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    drawTriangle(x,0,width)
    pen.end_fill()
    pen.begin_fill()
    drawUpsideDownTriangle(x, width/2,width)
    pen.end_fill()

def drawTree(x,width):
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()
    drawTriangle(x, -10, width)
    pen.end_fill()
    pen.begin_fill()
    drawTriangle(x+5,10,width/1.25)
    pen.end_fill()
    pen.begin_fill()
    drawTriangle(x+9,30,width/1.5)
    pen.end_fill()

def drawScene():
    sceneShape = getScene()
    x = -275
    for scene in sceneShape:
        if scene == "star":
            drawStar(x,50)
            x+=70
        if scene == "tree":
            drawTree(x,50)
            x+=70


drawScene()
turtle.done()