# Author: Sloane Luckiewicz

# set up
import random 
import turtle 
pen = turtle.Turtle()
turtle.setup(575,575)
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
pen.pencolor("black")
turtle.bgcolor("mintcream")

rubicsColors = ("red", "blue", "yellow", "orange", "green", "white")

# draw square
def draw_square(x,y,width,rubicsColors):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    color = random.choice(rubicsColors)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

# stack 3x3 square
def draw_rubics_cube(x,y,size):
    for i in range(3):
        for i in range(3):
            draw_square(x,y,size,rubicsColors)
            x+=size
        x-=size*3
        y+=size

# draw 10 rubics cubes
def draw_10_cubes():
    for i in range(10):
        size = random.randint(20,100)/2
        x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/3.5))
        y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/3))
        
        draw_rubics_cube(x,y,size)

draw_10_cubes()

turtle.done()