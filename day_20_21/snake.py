from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_LENGTH_OF_SNAKE = 3
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
UP = 90
LEFT = 0
RIGHT = 180
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self) -> None:
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            pass

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            pass

    def left(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            pass

    def right(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            pass

    def check_if_hit_wall(self) -> bool:
        return abs(self.head.xcor()) > SCREEN_WIDTH or abs(self.head.ycor()) > SCREEN_HEIGHT

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
