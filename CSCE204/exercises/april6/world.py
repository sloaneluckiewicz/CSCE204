import turtle 
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
pen.speed(0)

def getColors():
    colors = []

    # open file, read lines, and put in colors
    try:
        with open("exercises/april6/scene.txt") as file:
            for line in file:
                sceneColor = line.replace("\n", " ").strip().lower()
                colors.append(sceneColor)
    except FileNotFoundError:
        print("Sorry invalid file")

    return colors

def drawColorStrip(y, height, color):
    pen.up()
    pen.setpos(-int(turtle.window_width()/2),y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    
    for i in range(4):
        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else:
            pen.forward(height)
        pen.left(90)
    
    pen.end_fill()

def saveScene(colorList):
    with open("exercises/april6/scene.txt", "w") as file:
        for sceneColor in colorList:
            file.write(sceneColor + "\n")

def changeColor(x,y):
    userColor = turtle.textinput("Colors", "Enter color: ")
    stripHeight = -turtle.window_height()/len(colorList)
    section = int(y // stripHeight)
    index = -section + (len(colorList)-1)//2 # magic math

    colorList[index] = userColor
    saveScene(colorList)
    drawColorStrip(section * stripHeight, stripHeight, userColor)

# get the colors, loop through and draw strips 
colorList = getColors()
height = int(turtle.window_height()/len(colorList))
y = -int(turtle.window_height()/2)

# loop through colors and draw strips 
for color in colorList:
    drawColorStrip(y, height, color)
    y+= height


turtle.onscreenclick(changeColor)

turtle.done()