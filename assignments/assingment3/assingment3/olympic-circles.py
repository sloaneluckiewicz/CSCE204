# Author: Sloane Luckiewicz

import turtle 
turtle.bgcolor("white")
turtle.setup(500,500)

# pen setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
size = turtle.numinput("Olympic Rings", "Size (1-10): " ,5,1,10)
circleRadius = size * 10

pen.pensize(size)

# black ring 
pen.up()
pen.color("black")
pen.setpos(0, circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# blue ring
pen.up()
pen.color("blue")
pen.setpos(circleRadius * -2.5,circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# red ring
pen.up()
pen.color("red")
pen.setpos(circleRadius * 2.5,circleRadius)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# gold ring
pen.up()
pen.color("gold")
pen.setpos(circleRadius * -1.25,circleRadius* -.05)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

# green ring
pen.up()
pen.color("green")
pen.setpos(circleRadius * 1.25,circleRadius* -.05)
pen.setheading(0)
pen.down()
pen.circle(circleRadius)

turtle.done()

