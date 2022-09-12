from turtle import Turtle


class Scoreboard(Turtle):
    __GAME_OVER_COMMUNICAT = "GAME OVER!"
    __FONT = ("Courier", 20, "normal")
    __ALIGN = "center"

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0
        self.update_level()

    def update_level(self):
        self.increase_level()
        self.clear()
        self.goto(-220, 240)
        self.write("Level: " + str(self.level), align=self.__ALIGN, font=self.__FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(self.__GAME_OVER_COMMUNICAT, align=self.__ALIGN,
                   font=self.__FONT)
