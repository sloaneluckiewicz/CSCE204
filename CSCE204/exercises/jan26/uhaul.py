# Sloane Luckiewicz

import turtle 
turtle.bgcolor("skyblue")
turtle.setup(500,500)

# set up pen 
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("red")
pen.hideturtle()
pen.speed(0)

# get the uhaul size
size = turtle.numinput( "U-Haul", "Size (1-10):" ,4,1,10)
uhualWidth = size * 50
boxWidth = uhualWidth * .75
cabWidth = uhualWidth - boxWidth
boxHeight = uhualWidth / 2
cabHeight = boxHeight / 2
tireRadius = uhualWidth * .1

# draw the UHaul Body 
pen.up()
pen.setpos(-uhualWidth/2, 0)
pen.down()
pen.begin_fill()
pen.forward(uhualWidth)
pen.left(90)
pen.forward(cabHeight)
pen.left(90)
pen.forward(cabWidth)
pen.right(90)
pen.forward(boxHeight-cabHeight)
pen.left(90)
pen.forward(boxWidth)
pen.left(90)
pen.forward(boxHeight)
pen.end_fill()

# UHaul left tire
pen.up()
pen.setheading(0)
pen.setpos(-uhualWidth/4, -tireRadius)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()

# right tire
pen.up()
pen.setheading(0)
pen.setpos(uhualWidth/4, -tireRadius)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()



turtle.done()