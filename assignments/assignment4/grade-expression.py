# Author: Sloane Luckiewicz

import turtle
turtle.bgcolor("light pink")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

# ask user to enter grades
grade = turtle.numinput("Grades" , "Enter Grade: ")
# face
headRadius = 200
pen.up()
pen.setheading(0)
pen.setpos(0,-headRadius)
pen.down()
pen.circle(headRadius)

# left eye
pen.up()
pen.setheading(0)
pen.setpos(-headRadius/3, headRadius/10)
pen.fillcolor("black")
pen.begin_fill()
pen.down()
pen.circle(20)
pen.end_fill()

# right eye
pen.up()
pen.setheading(0)
pen.setpos(headRadius/3, headRadius/10)
pen.fillcolor("black")
pen.begin_fill()
pen.down()
pen.circle(20)
pen.end_fill()

if grade >= 80:
    pen.up()
    pen.setpos(-headRadius * .4,-headRadius * .4)
    pen.down()
    pen.setheading(-60)
    pen.circle(headRadius/2,120) 
elif grade >= 70:
    pen.up()
    pen.setpos(-headRadius * .4,-headRadius * .4)
    pen.down()
    pen.setheading(0)
    pen.forward(170)
elif grade < 69:
    pen.up()
    pen.setpos(-headRadius * .4,-headRadius * .6)
    pen.down()
    pen.setheading(60)
    pen.circle(-headRadius/2,120)

turtle.done()