import arcade

from game.window import GameWindow


def start_window():
    game = GameWindow(320, 180, "Our Game!", True, False)
    game.setup()

    # Will keep the program running, until the user closes the window
    arcade.run()


if __name__ == "__main__":      # Should not be imported
    start_window()
