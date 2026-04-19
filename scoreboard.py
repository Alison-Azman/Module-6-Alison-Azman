from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.truck_score = 0
        self.player_score = 0
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Player {self.player_score}   Trucks: {self.truck_score}",
            align="center",
            font=("Arial", 16, "bold"))

    def player_point(self):
        self.player_score += 1
        self.update_score()

    def truck_point(self):
        self.truck_score += 1
        self.update_score()