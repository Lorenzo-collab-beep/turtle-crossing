from turtle import Turtle
import globals


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.__level = 1
        self.penup()
        self.hideturtle()
        self.color(globals.FONT_COLOR)
        self.goto(int(-globals.SCREEN_W/2) + globals.SCORE_LEFT_OFFSET, int(globals.SCREEN_H/2) - globals.SCORE_UP_OFFSET)
        self.draw_level()

    def draw_level(self):
        self.clear()
        self.write(f"Level: {self.__level}", False, "center", globals.FONT)

    def update_level(self):
        self.__level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", globals.FONT)

