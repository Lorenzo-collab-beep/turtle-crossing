from turtle import Turtle
import globals


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape(globals.PLAYER_SHAPE)
        self.shapesize(globals.PLAYER_SHAPESIZE[0], globals.PLAYER_SHAPESIZE[1])
        self.color(globals.PLAYER_COLOR)
        self.setheading(90)
        self.goto(globals.STARTING_POSITION)

    def move(self):
        self.forward(globals.MOVE_DISTANCE)

    def reset(self):
        self.goto(globals.STARTING_POSITION)