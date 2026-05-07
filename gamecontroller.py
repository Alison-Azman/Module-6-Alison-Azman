
from turtle import Screen, mainloop
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

class GameController:
    def __init__(self, snake:Snake, food:Food, scoreboard:Scoreboard ):
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.is_game_on = True
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.bgcolor("blue")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

    def setup_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def run_game_loop(self):
        self.setup_bindings()
        self.food.refresh()
        self.scoreboard.update_scoreboard()
        while self.is_game_on:

            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            self.check_food_collision()
            self.check_wall_collision()
            self.check_self_collision()
        mainloop()

    def check_food_collision(self):
        if self.snake.head.distance(self.food) < 20:
            self.snake.grow()
            self.food.refresh()
            self.scoreboard.increase_score()

    def check_wall_collision(self):
        x_pos=self.snake.head.xcor()
        y_pos=self.snake.head.ycor()
        if x_pos>280 or x_pos<-280 or y_pos>280 or y_pos<-280:
            self.end_game()

    def check_self_collision(self):
        for seg in self.snake.segments[1:]:
            if self.snake.head.distance(seg) < 10: #check
                self.end_game()


    def end_game(self):

        self.is_game_on = False
        self.scoreboard.game_over()

if __name__ == "__main__":
    screen = Screen()
    screen.title("Snake Game")
    screen.bgcolor("blue")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    scoreboard = Scoreboard()
    snake = Snake()
    food = Food()
    gamecontroller = GameController(snake, food, scoreboard)
    gamecontroller.run_game_loop()
