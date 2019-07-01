import arcade


def _has_been_clicked(x, y, sprite):
    """ Returns a True if the coordinates are inside the sprite."""
    return sprite.left < x < sprite.right and sprite.bottom < y < sprite.top


class GameWindow(arcade.Window):
    """
    Main window for GAME
    """

    def __init__(self, width, height, title, fullscreen, resizable):
        """ Main window's initializer"""
        super().__init__(width, height, title, fullscreen, resizable)

        arcade.set_background_color(arcade.color.AMAZON)
        
        self.start_buttons = None

    def setup(self):
        """ Set up the game and initialize the variables.
        NOTE: This is ran here so we could restart the game."""
        self.start_menu()

    def start_menu(self):
        """ Will set up the window like the start menu """
        self.start_buttons = arcade.SpriteList()

        # I named the image cow.png but it is just a black box.
        self.start_button = arcade.Sprite("cow.png", 1)
        self.start_button.center_x, self.start_button.center_y = self.width/2, self.height/2
        self.start_buttons.append(self.start_button)

    # Events

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        self.start_buttons.draw()
        arcade.draw_text("Click Me!", self.start_buttons[0].left, self.start_buttons[0].bottom, arcade.color.WHITE, 31)

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
        print(_has_been_clicked(x, y, self.start_buttons[0]))

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
