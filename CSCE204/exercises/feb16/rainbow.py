import turtle
turtle.setup(575,575)
pen= turtle.Turtle()
pen.speed(0)
pen.pensize(5)
pen.hideturtle()

# make a tuple to hold the colors of the rainbow
colors = ("orchid", "slateblue", "dodgerblue", "lawngreen", "yellow", "orange", "tomato")
arcLength = 200
counter = 0

for color in colors:
    pen.up()
    pen.setpos(-arcLength/2, counter*10)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-arcLength,120)
    counter += 1

turtle.done()
