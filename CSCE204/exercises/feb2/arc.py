import turtle
turtle.bgcolor("light pink")
pen = turtle.Turtle()
pen.pensize(2)

# drawing a grid (horizontal line)
pen.up()
pen.setpos(-turtle.window_width()/2,0)
pen.down()
pen.forward(turtle.window_width())

# drawing a grid (vertical line)
pen.up()
pen.setpos(0, turtle.window_height()/2)
pen.setheading(270)
pen.down()
pen.forward(turtle.window_height())

# smile arc (concave up)
smileRadius = 100
"""
pen.up()
pen.setpos(-smileRadius,0)
pen.down()
pen.setheading(-60)
pen.circle(smileRadius,120)
"""

# frown arc (concave down)
pen.up()
pen.setpos(-smileRadius,0)
pen.down()
pen.setheading(60)
pen.circle(-smileRadius,120)


turtle.done()