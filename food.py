from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # food properties
        self.color("red")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        # regenerate the food at a random place
        x_pos = random.randint(-280,280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)