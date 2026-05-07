
from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_starting_snake()
        self.head = self.segments[0]

    def create_starting_snake(self):
        start_position = [(0, 0), (-20,0),(-40,0)]
        for position in start_position:
            segment = Turtle()
            segment.color("green")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)



    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def grow(self):
        tail=self.segments[-1]
        segment=Turtle()
        segment.color("green")
        segment.shape("square")
        segment.penup()
        segment.goto(tail.xcor(), tail.ycor())
        self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(0,0)
            segment.hideturtle()
        self.segments=[]
        self.create_starting_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() !=  270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
