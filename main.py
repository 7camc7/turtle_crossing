import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move_across()

    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    if turtle.finish_line():
        turtle.go_to_start()
        car.increase_speed()
        score.next_level()

screen.exitonclick()