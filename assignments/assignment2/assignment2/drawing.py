# Sloane Luckiewicz
import turtle 
turtle.bgcolor("sky blue")

# setting up pen
pen = turtle.Turtle()
pen.pensize(5)
pen.color("black")

# left ear
pen.up()
pen.setpos(-45,210)
pen.setheading(0)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# right ear
pen.up()
pen.setpos(45,210)
pen.setheading(0)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# arms
pen.up()
pen.setpos(-150,60)
pen.setheading(0)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.forward(300)
pen.right(90)
pen.forward(55)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(55)
pen.end_fill()

#  body
pen.up()
pen.setheading(0)
pen.setpos(0,-100)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# left foot
pen.up()
pen.setheading(0)
pen.setpos(-60,-130)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# right foot
pen.up()
pen.setheading(0)
pen.setpos(60,-130)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# head
pen.up()
pen.setheading(0)
pen.setpos(0,75)
pen.down()
pen.fillcolor("maroon")
pen.begin_fill()
pen.circle(75)
pen.end_fill()

# left eye
pen.up()
pen.setheading(0)
pen.setpos(-30,150)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# right eye
pen.up()
pen.setheading(0)
pen.setpos(30,150)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

turtle.done()