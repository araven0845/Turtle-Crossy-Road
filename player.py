from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("white")
        self.seth(90)

    def move(self):
        self.fd(MOVE_DISTANCE)


    def level_up(self):
        self.goto(STARTING_POSITION)


