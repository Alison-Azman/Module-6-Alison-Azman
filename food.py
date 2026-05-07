import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()

    def refresh(self):
        x,y=self.random_position()
        self.goto(x,y)

    def random_position(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        return x,y

