import time
from turtle import Turtle, Screen

from day_23.player import Player
from day_23.scoreboard import Scoreboard
from day_23.car_manager import CarManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("My crossroads game")
screen.tracer(0)

game_is_on = True
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Put cars on map
    car_manager.create_car()
    car_manager.move_cars()
    # Check if player ended level
    if player.ycor() > 280:
        player.new_level()
        scoreboard.update_level()
        car_manager.increase_speed()
    # Check if player has been hit by the car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
