import arcade
import random

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
            self.cow_list.append(cow.Cow(cow.CowBreed.meat,
                                 random.randint(constants.COW_IMAGE_WIDTH/2,
                                                constants.SCREEN_WIDTH),
                                 random.randint(constants.COW_IMAGE_HEIGHT/2,
                                                constants.SCREEN_HEIGHT)))

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
        self.cow_list.update()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.cow_list.on_pressed(x, y)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        self.cow_list.on_release(x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """
        Called when a user moves the mouse while pressing a button.
        """
        self.cow_list.on_mouse_drag(x, y)
