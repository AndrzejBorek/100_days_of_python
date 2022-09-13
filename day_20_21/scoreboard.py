from turtle import Turtle


class Scoreboard(Turtle):
    __ALIGN = "center"
    __FONT_NAME = "Arial"
    __FONT_SIZE = 24
    __FONT_TYPE = "normal"
    __FONT = (__FONT_NAME, __FONT_SIZE, __FONT_TYPE)
    __GAME_OVER_COMMUNICAT = "GAME OVER!"

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("record.txt") as file:
            content = file.read()
        self.high_score = int(content)
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=self.__ALIGN,
                   font=self.__FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(self.__GAME_OVER_COMMUNICAT, align=self.__ALIGN,
    #                font=self.__FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("record.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
