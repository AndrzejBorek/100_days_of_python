import turtle
from turtle import Screen, Turtle
import time

from day_20_21.snake import Snake
from day_20_21.food import Food
from day_20_21.scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
#
# turtle = Turtle()
# turtle.setheading()


game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with wall
    if snake.check_if_hit_wall():
        scoreboard.reset()
        snake.reset()
    # Detect collision with food
    if food.distance(snake.head) < 15:
        food.go_to_random_location()
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
