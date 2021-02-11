import turtle 
turtle.bgcolor("light green")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")
pen.hideturtle()
pen.speed(0)
size = 200

# center in the screen 
shape = turtle.textinput("Shape", "Enter Shape: ") .lower() .strip()
pen.up()
pen.setpos(-size/2, -size/2)
pen.down()

# ask the user for which shape
# then draw the shape
if shape == "square":
    # draw a square
    for i in range (4):
        pen.forward(size)
        pen.left(90)
elif shape == "triangle":
    # draw a triangle
    for i in range (3):
        pen.forward(size)
        pen.left(120)
elif shape == "star":
    # draw the star of david
    # right side up
    for i in range (3):
        pen.forward(size)
        pen.left(120)
# reset y coordinates to make the star    
    pen.up()
    pen.sety(0)
    pen.down()

    # upside down
    for i in range (3):
        pen.forward(size)
        pen.right(120)
        
turtle.done()