from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#86e7b8")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
        
    def move_right(self):
        self.goto(self.xcor()+20, self.ycor())
        
    def move_left(self):
        self.goto(self.xcor()-20, self.ycor())
        
    
        
    
    