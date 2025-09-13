import random
import turtle
import globals


class EnemiesManager:
    def __init__(self):
        self.__enemies_list = []
        self.__move_distance = globals.STARTING_MOVE_DISTANCE
        self.__random_seed = 0
        turtle.register_shape("custom_enemy", globals.ENEMY_SHAPE)

    def generate_enemies(self):
        random.seed(self.__random_seed)
        self.__random_seed += 1
        for i in range(globals.ENEMY_NUMBER):
            self.__enemies_list.append(self.__generate_enemy())

    def move_enemies(self):
        for enemy in self.__enemies_list:
            if int(enemy.xcor()) < int(-globals.SCREEN_W / 2):
                self.__packman_effect(enemy)
            enemy.forward(self.__move_distance)

    def speed_up_enemies(self):
        self.__move_distance += globals.MOVE_INCREMENT

    def clear_enemies(self):
        for enemy in self.__enemies_list:
            enemy.hideturtle()
        self.__enemies_list.clear()

    def detect_impact(self, player):
        for enemy in self.__enemies_list:
            if enemy.distance(player) < globals.TURTLE_DEFAULT_LEN - 1:
            # if ((abs(car.ycor() - player.ycor()) < globals.TURTLE_DEFAULT_LEN)
            #         and (abs(car.xcor() - player.xcor()) < globals.TURTLE_DEFAULT_LEN)):
                return True
        return False

    @staticmethod
    def __generate_enemy():
        enemy = turtle.Turtle()
        enemy.penup()
        enemy.setheading(180)
        enemy.shape("custom_enemy")
        enemy.shapesize(globals.ENEMY_SHAPESIZE[0], globals.ENEMY_SHAPESIZE[1])
        enemy.color(random.choice(globals.COLORS_LIST))
        enemy.goto(random.randint(int(globals.SCREEN_W / 2), int(globals.SCREEN_W / 2) + globals.SCREEN_W),
                   random.randint(int(-globals.SCREEN_H/2) + globals.STREET_OFFSET, int(globals.SCREEN_H/2) - globals.STREET_OFFSET))
        return enemy

    @staticmethod
    def __packman_effect(enemy):
        enemy.goto(int(globals.SCREEN_W/2), int(enemy.ycor()))