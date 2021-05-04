# Author: Sloane Luckiewicz
# Hangman Man
style = ("Courier", 40)
class Man:
    def __init__(self, width, appendage, outcome):
        self.width = width 
        self.appendage = appendage
        self.outcome = outcome
        self.style = ("Courier", 20)

    def draw(self,pen):
        pen.penup()
        pen.setpos(0,75)
        pen.pendown()

        if self.appendage == 1:
            self.draw_head(pen)
        elif self.appendage == 2:
            self.draw_torso(pen)
        elif self.appendage == 3:
            self.draw_arm1(pen)
        elif self.appendage == 4:
            self.draw_arm2(pen)
        elif self.appendage == 5:
            self.draw_leg1(pen)
        elif self.appendage == 6:
            self.draw_leg2(pen)
        elif self.appendage == 7:
            self.draw_eyes(pen)
        elif self.appendage == 8:
            self.draw_frown(pen)
        elif self.appendage == 9:
            self.draw_hat(pen)
        if self.outcome ==1:
            self.write_winner(pen)

    def draw_head(self,pen):
        pen.circle(self.width/2)
        pen.penup()
        pen.setpos(-150,-200)
        pen.pendown()
        pen.setheading(0)

    def draw_torso(self,pen):
        pen.penup()
        pen.setpos(2,76)
        pen.setheading(270)
        pen.pendown()
        pen.forward(self.width)
        pen.setheading(0)
            
    def draw_arm1(self,pen):
        pen.penup()
        pen.setpos(2,50)
        pen.setheading(180)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def draw_arm2(self,pen):
        pen.penup()
        pen.setpos(2,50)
        pen.setheading(360)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def draw_leg1(self,pen):
        pen.penup()
        pen.setpos(2,25)
        pen.setheading(220)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def draw_leg2(self,pen):
        pen.penup()
        pen.setpos(2,25)
        pen.setheading(320)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def draw_eyes(self,pen):
        pen.up()
        pen.setpos(-5,100)
        pen.setheading(0)
        pen.pendown()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(self.width/35)
        pen.end_fill()
        pen.up()
        pen.setpos(5,100)
        pen.setheading(0)
        pen.pendown()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(self.width/35)
        pen.end_fill()

    def draw_frown(self,pen):
        pen.up()
        pen.setpos(4,87)
        pen.down()
        pen.setheading(60)
        pen.circle(self.width/12,240)
        pen.setheading(0)

    def draw_hat(self,pen):
        pen.up()
        pen.pensize(3)
        pen.setpos(-30,125)
        pen.down()
        pen.forward(self.width*1.17)
        pen.up()
        pen.pensize(2)
        pen.setpos(-13,125)
        pen.fillcolor("black")
        pen.begin_fill()
        for i in range (4):
            pen.forward(self.width/2)
            pen.left(90)
        pen.end_fill()
        pen.penup()
        pen.setpos(-75,-75)
        style = ("Courier", 40)
        pen.write("You Lose!", font = style)

    def write_winner(self,pen):
            pen.penup()
            pen.setpos(-75,-75)
            pen.pendown()
            style = ("Courier", 40)
            pen.write("Winner!", font = style)
