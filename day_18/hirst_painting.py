import colorgram
import turtle as t
import random

colours = colorgram.extract('dots.jpg', 10)

list_of_colours = []

for color in colours:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    list_of_colours.append((r, g, b))

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)
timmy.speed("fastest")
timmy.penup()
x_coord = -370
y_coord = -290
timmy.goto(x_coord, y_coord)

screen = t.Screen()


def hirst_painting():
    timmy.hideturtle()
    global y_coord
    for i in range(10):
        for j in range(10):
            timmy.dot(20, random.choice(list_of_colours))
            timmy.forward(screen.window_width() / 10)
        y_coord = y_coord + screen.window_height() / 10
        timmy.goto(x_coord, y_coord)


hirst_painting()

screen.exitonclick()
