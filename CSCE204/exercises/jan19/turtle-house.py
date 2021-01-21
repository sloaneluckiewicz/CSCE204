import turtle
turtle.bgcolor("purple")

# setting up pen
pen = turtle.Turtle()
pen.pensize(5)
pen.color("green")


# house body
pen.up()
pen.setpos(-100,100)
pen.down()
pen.fillcolor("pink")
pen.begin_fill()
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.left(90)
pen.end_fill()


# house roof
pen.up()
pen.setheading(0)
pen.setpos(-100,100)
pen.fillcolor("red")
pen.begin_fill()
pen.down()
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.end_fill()

# door
pen.up()
pen.setheading(0)
pen.setpos(-25,-100)
pen.fillcolor("green")
pen.down()
pen.begin_fill()
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.end_fill()

# door knob
pen.up()
pen.setheading(0)
pen.setpos(30,-75)
pen.down()
pen.fillcolor("brown")
pen.begin_fill()
pen.circle(10)
pen.end_fill()



turtle.done()