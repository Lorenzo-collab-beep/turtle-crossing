# CONSTANTS

# window
SCREEN_W = 600
SCREEN_H = 600

# loop
GAME_REFRESH_SPEED = 100

# icon
CROSSING_ICON = "assets/crossing_ico.png"

# music
GAME_MP3 = "assets/8-bit-game.mp3"
GAME_OVER_SOUND = "assets/death-sound.mp3"
VOLUME = 0.5

# font
FONT = ("Impact", 30, "normal")
FONT_COLOR = "black"

# score
SCORE_LEFT_OFFSET = 70
SCORE_UP_OFFSET = 50

# enemies
COLORS_LIST = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
ENEMY_NUMBER = 20
STREET_OFFSET = 70
ENEMY_SHAPESIZE = (1, 2)
ENEMY_SHAPE = (
    (-5, -10), (5, -10), (5, 10), (10, 5), (-10, 5), (-5, 10) # SPANNER
    #(0, -10), (0, 10), (20, 10), (20, -10) # SQUARE
)

# player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_COLOR = "DarkSlateGray"
TURTLE_DEFAULT_LEN = 20
PLAYER_SHAPESIZE = (1, 1)
PLAYER_SHAPE = "turtle"
