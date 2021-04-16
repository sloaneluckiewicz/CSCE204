from house import House 
import turtle 
turtle.setup(800,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

houses = (
    House(pen, "1 A Street", -200, 0, 50, "medium aquamarine", "hot pink", True),
    House(pen, "2 A Street", -100, 0, 50, "dark orchid", "lime green", False),
    House(pen, "3 A Street", 0, 0, 50, "orange red", "gold", False),
    House(pen, "4 A Street", 100, 0, 50, "honeydew", "powder blue", False),
    House(pen, "5 A Street", 200, 0, 50, "light pink", "lavender", True)
)

# loop through the houses and draw them 
for house in houses:
    house.draw()


turtle.done()