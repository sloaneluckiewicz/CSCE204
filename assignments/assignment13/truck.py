# Author: Sloane Luckiewicz
# OOP part 3

class Truck:
    def __init__(self, pen, x, y, height, color, extended_cab, xlong_bed):
        self.pen = pen
        self.x = x
        self.y = y
        self.height = height 
        self.color = color 
        self.extended_cab = extended_cab
        self.xlong_bed = xlong_bed

    def draw(self):
        self.pen.up()
        self.pen.setpos(self.x, self.y)
        self.pen.down()
        self.draw_truck_body(pen)
        self.draw_truck_cab(pen)

    # truck body
    def draw_truck_body(self, pen):
        self.pen.up()
        self.pen.setpos(self.x,self.y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        if xlong_bed:
            for i in range (4):
                if i % 2 == 0:
                    self.pen.forward(self.width*2)
                else:
                    self.pen.forward(self.width*2)
                self.pen.left(90)
        else:
            for i in range (4):
                if i % 2 == 0:
                    self.pen.forward(self.width)
                else:
                    self.pen.forward(self.height)
                self.pen.left(90)

        self.pen.end_fill()

    def draw_truck_cab(self, pen):
        self.pen.up()
        self.pen.setpos(self.x + 25, self.y +25)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        if extended_cab:
            for i in range (4):
                if i % 2 == 0:
                    self.pen.forward(self.width*2)
                else:
                    self.pen.forward(self.width*2)
        else:
            for i in range (4):
                if i % 2 == 0:
                    self.pen.forward(self.width)
                else:
                    self.pen.forward(self.width)
        self.pen.end_fill()

