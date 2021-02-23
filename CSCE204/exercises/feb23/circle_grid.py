import turtle 
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
turtle.bgcolor("lavenderblush")

gridSize = int(turtle.numinput("Size", "Enter size: ", 5,1,10))
diameterPadding = turtle.window_width()/gridSize
padding = diameterPadding * .1
radius = diameterPadding * .8 / 2

for row in range(gridSize):
    x = -turtle.window_width()/2 + diameterPadding/2
    y= -turtle.window_height()/2 + padding + diameterPadding * row
    
    for col in range(gridSize):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.circle(radius) 
        x += diameterPadding
    
           
turtle.done()