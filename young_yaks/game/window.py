import arcade


class GameWindow(arcade.Window):
    """
    Main window for GAME
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        pass

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass
