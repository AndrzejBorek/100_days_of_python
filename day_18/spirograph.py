import turtle as t
import random

timmy = t.Turtle()

timmy.shape("turtle")
t.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def spirograph(circles):
    for i in range(circles):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(360/circles)


spirograph(360)

screen = t.Screen()
screen.exitonclick()
