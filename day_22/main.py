from turtle import Screen, Turtle

from day_22.ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with top or bottom wall
    if abs(ball.ycor()) >= 290:
        ball.bounce_off_wall()
    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50) and abs(ball.xcor()) > 330:
        ball.bounce_off_paddle()
    # Detect if ball has missed a right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_left_score()

    # Detect if ball has missed a left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_right_score()

screen.exitonclick()
