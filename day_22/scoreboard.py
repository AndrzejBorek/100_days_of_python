from turtle import Turtle


class Scoreboard(Turtle):
    __FONT = ("Courier", 80, "normal")

    def __init__(self, ):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_points()

    def update_points(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=self.__FONT)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=self.__FONT)

    def add_left_score(self):
        self.left_score += 1
        self.update_points()

    def add_right_score(self):
        self.right_score += 1
        self.update_points()
