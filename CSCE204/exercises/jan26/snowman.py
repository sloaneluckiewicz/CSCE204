import turtle 
turtle.bgcolor("skyblue")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")
pen.hideturtle()
pen.speed(0)

# turtle.numinput("Title", "Prompt", ""default", "min", "max") 
size = turtle.numinput("Snowman", "Size (1-4): " ,3,1,4)
lgRadius = size * 20
medRadius = size * 15
smRadius = size * 10
eyeRadius = size * 2
noseSize = size * 4

# draw the bottom circle 
pen.up()
pen.setpos(0, -2*lgRadius)
pen.down()
pen.begin_fill()
pen.circle(lgRadius)
pen.end_fill()

# draw medium circle 
pen.up()
pen.setpos(0,0)
pen.down()
pen.begin_fill()
pen.circle(medRadius)
pen.end_fill()

# draw small circle 
pen.up()
pen.setpos(0, medRadius*2)
pen.down()
pen.begin_fill()
pen.circle(smRadius)
pen.end_fill()

# draw right eye
pen.up()
pen.setpos(smRadius/3, (medRadius*2)+smRadius)
pen.fillcolor("black")
pen.down()
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

# draw left eye 
pen.up()
pen.setpos(-smRadius/3, (medRadius*2)+smRadius)
pen.fillcolor("black")
pen.down()
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

# draw nose
pen.up()
pen.setpos(0, (2*medRadius)+0.5*smRadius)
pen.fillcolor("orange")
pen.down()
pen.begin_fill()

# nose first line
pen.setheading(60)
pen.forward(noseSize)

# nose second line 
pen.left(120)
pen.forward(noseSize)

# nost third line
pen.left(120)
pen.forward(noseSize)

pen.end_fill()

turtle.done()
