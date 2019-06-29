import arcade

from window import GameWindow

if __name__ == "__main__":      # Should not be imported
    game = GameWindow(1680, 1050, "Our Game!")
    game.setup()

    # Will keep the program running, until the user closes the window
    arcade.run()
