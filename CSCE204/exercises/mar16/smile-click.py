import turtle 
pen = turtle.Turtle()
turtle.setup(575,575)
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
pen.pencolor("black")
turtle.bgcolor("lightsteelblue")

smileRadius = 30

def draw_smiley(x,y):
    draw_head(x,y)
    draw_eye(x-smileRadius/3,y)
    draw_eye(x+smileRadius/3,y)
    draw_mouth(x-smileRadius/2.5, y-smileRadius/3)

def draw_head(x,y):
    pen.up()
    pen.setpos(x,y-smileRadius)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("yellow")
    pen.circle(smileRadius)
    pen.end_fill()

def draw_eye(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(smileRadius/8)
    pen.end_fill()
    
def draw_mouth(x,y):
    mouthRadius = smileRadius/2
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(-60)
    pen.circle(mouthRadius,120)
    pen.setheading(0)

turtle.onscreenclick(draw_smiley)

turtle.done()