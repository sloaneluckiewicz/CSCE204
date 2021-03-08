# Author: Sloane Luckiewicz
# Midterm

import turtle 
turtle.setup(500,500)
pen = turtle.Turtle()

pen.hideturtle()
turtle.bgcolor("lavenderblush")
pen.pensize(2)
pen.pencolor("black")
pen.up()
pen.setpos(-225,200)
pen.down()
pen.write("Food Order: ", font=('arial',20)) 


# lists
quantityList = []
nameList = []
mealList = []
sideList = []
drinkList = ["apple", "orange"]


# order & quantity
quantity = int(turtle.numinput("Order Quantity", "How many orders would you like? : ", 2,1,6))

# variables
orderSize = 50
x= -turtle.window_width()/2
y= -turtle.window_height()/100
widthPadding = ((orderSize / x) + 50)
heightPadding = orderSize / y 


for i in range (quantity):
    forwardAmount = orderSize+widthPadding 
    name = turtle.textinput("Name", "Enter the name for the order: ") .lower() .strip()
    nameList.append(name)
    pen.up()
    pen.setpos(x - widthPadding + forwardAmount, y+ heightPadding)
    pen.down()
    pen.write(nameList[i], font=('arial',14))

    
    meal = turtle.textinput("Meal", "Enter the meal for the order (pancakes, waffles, parfait): ") .lower() .strip()
    mealList.append(meal)
    pen.up()
    pen.setpos(x + widthPadding,y+ (heightPadding)-20)
    pen.down()
    pen.write(mealList[i], font=('arial',14))


    side = turtle.textinput("Side", "Enter the side for the meal (bacon, potatoes, toast): ") .lower() .strip()
    sideList.append(side)
    pen.up()
    pen.setpos(x + widthPadding, y+ (heightPadding) -40)
    pen.down()
    pen.write(sideList[i], font=('arial',14))
   

    drink = turtle.textinput("Drink", "Enter the juice for each order (apple, orange): ") .lower() .strip()
    drinkList.append(drink)

    
    
    # apple
    if drinkList[i] == "apple":
        pen.up()
        pen.setpos(x + widthPadding+ forwardAmount/3.25,y+ (-heightPadding) -125)
        pen.down()
        pen.fillcolor("red")
        pen.begin_fill()
        pen.circle(orderSize/2)
        pen.up()
        pen.setpos(x + widthPadding+forwardAmount/3.85, y+(-heightPadding)-80)
        pen.down()
        pen.end_fill()
        pen.fillcolor("brown")
        pen.begin_fill()
        for i in range(4):
            pen.forward(orderSize/4)
            pen.left(90)
        pen.end_fill()

    elif drinkList[i] == "orange":
        pen.up()
        pen.setpos(x + widthPadding+ forwardAmount/3.25,y+ (-heightPadding) -125)
        pen.down()
        pen.fillcolor("orange")
        pen.begin_fill()
        pen.circle(orderSize/2)
        pen.end_fill()

    x+= forwardAmount

turtle.done()