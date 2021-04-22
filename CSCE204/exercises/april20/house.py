import turtle
import shapes as sh

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("azure")

sh.draw_square(pen, -50,-50, 100)
sh.draw_triangle(pen, -70, 50,140)
sh.draw_rectangle(pen, -15, -50, 50, 30)

turtle.done()