import turtle as t
import random as r

# from turtle import *

timmy = t.Turtle()

timmy.shape("turtle")

# timmy.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


#
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# def square(turtle):
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#
#
# def triangle(turtle):
#     for i in range(3):
#         if i == 1:
#             turtle.forward(100 * math.sqrt(2))
#         else:
#             turtle.forward(100)
#         turtle.right(135)
#
#
# def dashedLine(turtle):
#     for i in range(20):
#         if i % 2 == 0:
#             turtle.pendown()
#         else:
#             turtle.penup()
#         turtle.forward(10)


# dashedLine(timmy)
# square(timmy)
# triangle(timmy)
# def TicTacToeBoard_Start(turtle):
#     turtle.penup()
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(270)
#     turtle.pendown()
#
#
# def TicTacToeBoard_HorizontalLine(turtle):
#     turtle.forward(300)
#     turtle.right(180)
#     turtle.forward(600)
#     turtle.right(180)
#     turtle.forward(400)
#
#
# def TicTacToeBoard_DiagonalLine(turtle):
#     turtle.forward(200)
#     turtle.right(180)
#     turtle.forward(600)
#     turtle.right(180)
#
#
# def ticTacToeBoard_Whole(turtle):
#     TicTacToeBoard_Start(turtle)
#     TicTacToeBoard_HorizontalLine(turtle)
#     turtle.right(90)
#     TicTacToeBoard_DiagonalLine(turtle)
#     turtle.forward(400)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(270)
#     TicTacToeBoard_DiagonalLine(turtle)
#     turtle.forward(200)
#     turtle.right(270)
#     turtle.forward(100)
#     TicTacToeBoard_HorizontalLine(turtle)


# ticTacToeBoard_Whole(timmy)

def draw_n_gon_shape(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)


for side in range(3, 11):
    timmy.color(r.choice(colours))
    draw_n_gon_shape(side)

screen = t.Screen()
screen.exitonclick()
