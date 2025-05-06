from turtle import Turtle
import random
STARTING_POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # define snake head
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        # creating a snake of 3 blocks
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        # defining properties of the snake segments
        my_turtle = Turtle()
        my_turtle.shape("square")
        my_turtle.penup()
        my_turtle.color("white")
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def extend(self):
        # extend the length of the snake for every point taken
        self.add_segment(self.segments[-1].position())

    def move(self):
        # move all the snake segments together
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # controlling movements for the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

