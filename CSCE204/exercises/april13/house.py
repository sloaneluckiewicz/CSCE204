class House:
    def __init__(self, pen, address, x, y, width, building_color, roof_color, chimney):
        self.pen = pen
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.building_color = building_color
        self.roof_color = roof_color
        self.chimney = chimney
        self.style = ("Arial", int(width/4), "bold")

    def draw(self):
        self.pen.up()
        self.pen.setpos(self.x, self.y)
        self.pen.down()
        self.draw_house_base()
        self.draw_roof()
        self.draw_chimney()
        self.write_address()
        self.draw_door()
        
    def draw_house_base(self):
        self.pen.fillcolor(self.building_color)
        self.pen.begin_fill()
        for i in range (4):
            self.pen.forward(self.width)
            self.pen.left(90)
        self.pen.end_fill()
        
    def draw_chimney(self):
            if self.chimney:
                chimney_width = self.width * .2
                self.pen.up()
                self.pen.setpos(self.x + self.width *.1, self.y + self.width * 1.5)
                self.pen.down()
                self.pen.fillcolor(self.building_color)
                self.pen.begin_fill()
            
                for i in range (4):
                    if i % 2 == 0:
                        self.pen.forward(chimney_width)
                    else:
                        self.pen.forward(chimney_width * 3)
                    self.pen.left(90)
                self.pen.end_fill()

    def draw_roof(self):
        roof_width = self.width * 1.4
        self.pen.up()
        self.pen.setpos(self.x - self.width * .2, self.y + self.width)
        self.pen.down()
        self.pen.fillcolor(self.roof_color)
        self.pen.begin_fill()
        for i in range (3):
            self.pen.forward(roof_width)
            self.pen.left(120)
        self.pen.end_fill()

    def draw_door(self):
        door_width = self.width * .3
        self.pen.up()
        self.pen.setpos(self.x + self.width * .35, self.y)
        self.pen.down()
        self.pen.fillcolor(self.roof_color)
        self.pen.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                self.pen.forward(door_width)
            else:
                self.pen.forward(door_width)
            self.pen.left(90)
        self.pen.end_fill()
       
    def write_address(self):
        self.pen.up()
        self.pen.setpos(self.x - self.width * .7, self.y - self.width * 1.1)
        self.pen.down()
        self.pen.write(self.address, font = self.style)

   


