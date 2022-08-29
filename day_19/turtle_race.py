import random
from turtle import Turtle, Screen

screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
answer = screen.textinput(title="Guess the winner", prompt="Enter the colour of who do you think will win")
colors = ["red", "green", "yellow", "blue", "purple", "orange"]

is_race_on = False

if answer:
    is_race_on = True


def setup_turtles():
    all_turtles = []
    for i in range(len(colors)):
        all_turtles.append(Turtle("turtle"))
        all_turtles[i].color(colors[i])
    y_coord = -120
    x_coord = -225
    for turtle in all_turtles:
        turtle.penup()
        turtle.goto(x=x_coord, y=y_coord)
        y_coord = y_coord + 50
    return all_turtles


turtles = setup_turtles()


def move_random_turtle():
    global is_race_on
    turtle = random.choice(turtles)
    turtle.forward(random.randint(0, 10))
    if turtle.pos()[0] >= width / 2:
        if turtle.color()[0] == answer:
            print("You have guess the winner!")
        else:
            print(f"You failed to guess the winner, the winner was {turtle.color()[0]}")
        is_race_on = False
    # else:
    #     pass


def race():
    while is_race_on:
        move_random_turtle()
    else:
        screen.clear()


race()
screen.exitonclick()
