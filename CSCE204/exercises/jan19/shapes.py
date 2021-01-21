import turtle
turtle.bgcolor("lightpink")

# setting up our pen
pen = turtle.Turtle()
pen.pensize(5)
pen.color("purple")

# square
pen.fillcolor("green")
pen.begin_fill()
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.end_fill()

# triangle
pen.up()
pen.setpos(-200,100)
pen.down()
pen.setheading(0)
pen.fillcolor("turquoise")
pen.begin_fill()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.end_fill()

# upside down triangle
pen.up()
pen.setpos(-200,-200)
pen.down()
pen.setheading(0)
pen.fillcolor("yellow")
pen.begin_fill()
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.end_fill()

# circle
pen.up()
pen.setpos(200,-200)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(45)
pen.end_fill()

turtle.done()