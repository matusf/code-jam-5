import arcade

from . import background
from .models import Game


class GameWindow(arcade.Window):
    """
    Main window for GAME
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable)

        # All variables are later defined in setup.
        # This is so we can restart the game.
        self.background: background.Background

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        self.background = background.StartBackground()  # We always start in the start menu
        self.game = Game.init_game()

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.background.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.game.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        # If we're in the start "menu":
        if isinstance(self.background, background.StartBackground):
            self.background = background.GameBackground()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # If we're in the start "menu":
        if isinstance(self.background, background.StartBackground):
            self.background = background.GameBackground()
