import arcade


class GameWindow(arcade.Window):
    """
    Main window for the game.
    """

    def __init__(self, width, height, title, fullscreen, resizable, antialiasing):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable, antialiasing=antialiasing)

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        pass

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        pass

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
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
