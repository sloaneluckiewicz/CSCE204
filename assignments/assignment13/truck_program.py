# Author: Sloane Luckiewicz
# OOP part 3

from truck import Truck
import turtle
turtle.bgcolor("skyblue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

# street
def draw_street(x, y, height, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range (4):
        if i % 2 == 0:
            pen.forward(width)
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

draw_street(-turtle.window_width()/2, -turtle.window_height()/8, turtle.window_height()/4, turtle.window_width, "gray")
x = 0
for i in range (5):
    draw_street(-turtle.window_width()/2, 0/-turtle.window_height()/60, turtle.window_height()/30, turtle.window_width()/6, "yellow")
    x += turtle.window_width()/5

trucks =[]
trucks.append(Truck(-265, 70, 20, "lavendar", False, True)),
trucks.append(Truck(-145, 70, 20, "navajo white", True, True)),
trucks.append(Truck(-50, 70, 20, "cornflower blue", False, False)),
trucks.append(Truck(-80, 70, 20, "spring green", True, False))

for truck in trucks:
    truck.draw()


turtle.done()