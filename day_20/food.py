import random
from turtle import Turtle


class Food(Turtle):
    __SAFE_WIDTH = 280
    __SAFE_HEIGHT = 280

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-self.__SAFE_WIDTH, self.__SAFE_WIDTH)
        random_y = random.randint(-self.__SAFE_HEIGHT, self.__SAFE_HEIGHT)
        self.goto(random_x, random_y)

    def go_to_random_location(self):
        random_x = random.randint(-self.__SAFE_WIDTH, self.__SAFE_WIDTH)
        random_y = random.randint(-self.__SAFE_HEIGHT, self.__SAFE_HEIGHT)
        self.goto(random_x, random_y)
