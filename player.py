from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

score = Scoreboard()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def hit_car(self):
        self.goto(STARTING_POSITION)
        score.reset_level()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False





