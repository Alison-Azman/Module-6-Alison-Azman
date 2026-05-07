import turtle

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 18, "bold"))

    def increase_score(self):
        self.score+=1
        if self.score>self.highscore:
            self.highscore=self.score
        self.update_scoreboard()


    def reset(self):
        self.score=0
        self.update_scoreboard()



    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 18, "bold"))
