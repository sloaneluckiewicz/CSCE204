import turtle 
turtle.bgcolor("skyblue")
turtle.setup(500,500)

# setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")

# turtle.numinput("Title", "Prompt", ""default", "min", "max") 
size = turtle.numinput("Snowman", "Size (1-4): " ,3,1,4)
lgRadius = size * 20

# draw the bottom circle 
pen.begin_fill()
pen.circle(lgRadius)
pen.end_fill()


turtle.done()
