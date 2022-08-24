import turtle as t
import random

timmy = t.Turtle()

timmy.shape("turtle")
t.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]

angles = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk(number_of_lines):
    timmy.speed(20)
    timmy.width(5)
    for _ in range(number_of_lines):
        timmy.pencolor(random_color())
        timmy.forward(20)
        timmy.setheading(random.choice(angles))


random_walk(400)

screen = t.Screen()
screen.exitonclick()
