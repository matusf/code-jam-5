from functools import partialmethod
import arcade

from . import background
from .models import Game
from .button import ActionButton


def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(x, y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()


class GameWindow(arcade.Window):
    """
    Main window for the game.
    """

    def __init__(self, width, height, title, fullscreen, resizable, antialiasing):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable, antialiasing=antialiasing)

        # All variables are later defined in setup.
        # This is so we can restart the game.
        self.background: background.Background
        self.button_list = None

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        self.background = background.StartBackground()  # We always start in the start menu
        self.game = Game.init_game()
        self.button_list = [
            ActionButton(
                action=partialmethod(self.game.buy_cow, "Meat Cows"),
                center_x=30,
                center_y=10,
                width=80,
                height=30,
                text="Buy Meat Cow"
            ),
            ActionButton(
                action=partialmethod(self.game.buy_cow, "Milk Cows"),
                center_x=30,
                center_y=50,
                width=80,
                height=30,
                text="Buy Milk Cow"
            ),
            ActionButton(
                action=partialmethod(self.game.buy_cow, "Meat Burp"),
                center_x=30,
                center_y=70,
                width=80,
                height=30,
                text="Buy Burp Cow"
            ),
            ActionButton(
                action=partialmethod(self.game.sell_cow, "Meat Cows"),
                center_x=100,
                center_y=10,
                width=80,
                height=30,
                text="Buy Meat Cow"
            ),
            ActionButton(
                action=partialmethod(self.game.sell_cow, "Milk Cows"),
                center_x=100,
                center_y=50,
                width=80,
                height=30,
                text="Buy Milk Cow"
            ),
            ActionButton(
                action=partialmethod(self.game.sell_cow, "Meat Burp"),
                center_x=100,
                center_y=70,
                width=80,
                height=30,
                text="Buy Burp Cow"
            ),
        ]

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.background.draw()
        for button in self.button_list:
            button.draw()

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
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)
