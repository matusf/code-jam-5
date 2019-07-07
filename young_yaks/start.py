import arcade
from game import constants

from game.window import GameWindow


def start_window():
    game = GameWindow(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_NAME,
                      constants.SCREEN_FULLSCREEN, constants.SCREEN_RESIZE,
                      constants.SCREEN_ALIASING)
    game.setup()

    # Will keep the program running, until the user closes the window
    arcade.run()


if __name__ == "__main__":      # Should not be imported
    start_window()
