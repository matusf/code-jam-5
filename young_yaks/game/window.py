import arcade

from . import models
from . import cow
from . import constants


class GameWindow(arcade.Window):
    """
    Main window for the game.
    """

    def __init__(self, width, height, title, fullscreen, resizable, antialiasing):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable, antialiasing=antialiasing)

        self.cow_list = None

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game.
        """

        self.cow_list = models.CowSpriteList()

        for i in range(constants.START_MENU_COWS):
            self.cow_list.append(cow.Cow(cow.CowBreed.meat, 1, 1))

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.cow_list.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
