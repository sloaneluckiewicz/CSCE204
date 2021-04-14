# Author: Sloane Luckiewicz 
# OOP Part 2

class Bird:
    def __init__(self, bird_type, color, food, description):
        self.bird_type = bird_type
        self.color = color
        self.food = food
        self.description = description
        self.bird = (bird_type, color, food, description)

    def display(self):
            print(f"""
        *** {self.bird_type} ***
        Color: {self.color}
        Food: {self.food}
        {self.description}
        """)

    def is_match(self, bird_name):
        if self.bird_type == True:
            return False
        if bird_name == self.bird_type:
            return True
        
        return False