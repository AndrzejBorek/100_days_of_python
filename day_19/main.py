from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()

screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=clear_screen, key="c")

screen.exitonclick()
