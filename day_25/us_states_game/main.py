import turtle

import pandas as pd
from turtle import Screen

screen = Screen()
screen.title('Guess the state game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Code to check what are the coords of my click on image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

data = pd.read_csv('50_states.csv')

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if not data[data.state == answer_state].empty:
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        turtle.goto(x=x, y=y)
        turtle.write(answer_state)
        guessed_states.append(answer_state)
    else:
        pass
    if answer_state == "Exit":
        missed_states = [state for state in data.state if state not in guessed_states]
        new_data = pd.DataFrame(missed_states).to_csv("missing_states.csv")
        break
