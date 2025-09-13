from player import Player
from enemies_manager import EnemiesManager
from scoreboard import Scoreboard
from window import setup_window, window_game_over, window_quit
import globals

def main():
    screen = setup_window()
    player = Player()
    scoreboard = Scoreboard()
    enemies_manager = EnemiesManager()

    enemies_manager.generate_enemies()

    screen.listen()
    screen.update()

    screen.onkeypress(player.move, "Up")

    def game_loop():
        enemies_manager.move_enemies()

        if player.ycor() > globals.SCREEN_H/2 - globals.TURTLE_DEFAULT_LEN:
            enemies_manager.clear_enemies()
            enemies_manager.generate_enemies()
            scoreboard.update_level()
            scoreboard.draw_level()
            player.reset()
            enemies_manager.speed_up_enemies()

        screen.update()

        if enemies_manager.detect_impact(player):
            scoreboard.game_over()
            window_game_over()
            return

        screen.ontimer(game_loop, globals.GAME_REFRESH_SPEED)

    game_loop()
    screen.mainloop()
    window_quit()


# main
if __name__ == "__main__":
    main()