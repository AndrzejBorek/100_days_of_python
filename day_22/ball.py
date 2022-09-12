import time
from turtle import Turtle
import random

DIRECTIONS = (-10, 10)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)
        self.y_move = random.choice(DIRECTIONS)
        self.x_move = random.choice(DIRECTIONS)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.x_move *= -1
