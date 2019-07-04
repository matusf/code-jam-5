import arcade
from .textbutton import TextButton
from .background import Background
from collections import UserList


class DrawList(UserList):
    """ A custom list tweaked to work with objects
    that implement the draw method."""
    def draw(self):
        """ Draw all the items."""
        for item in self.data:
            item.draw()


class GameWindow(arcade.Window):
    """
    Main window for GAME
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable)

        arcade.set_background_color(arcade.color.AMAZON)
        self.background = None
        self.draw_list = None
        self.start_draw_list = DrawList([
            TextButton(x=self.width/2, y=self.height/2, width=300, height=300,
                       text="Clicks ;)", font_size=12.0, color=(150, 150, 150),
                       text_color=(0, 0, 0), filled=True)])

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        self.background = Background(color=arcade.color.AMAZON)
        self.draw_list = self.start_draw_list

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.background.draw()
        self.draw_list.draw()

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

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(self.draw_list[0].is_inside(x, y))

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
