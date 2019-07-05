import arcade

from . import constants


class Background:
    """ A class representing a window background."""
    def __init__(self, texture=None, color=None):
        # To avoid error with loading a texture with None as parameter
        self.texture = None if texture is None else arcade.load_texture(texture)
        # We don't allow both attributes at the same time
        self.color = color if texture is None else None

    def draw(self):
        if self.texture:
            arcade.draw_texture_rectangle(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                                          constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                          self.texture)
        else:
            arcade.draw_rectangle_filled(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
                                         constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                         self.color)


class StartBackground(Background):
    """ The background you start with, this inherits from Background."""
    def __init__(self):
        super().__init__(texture="game/assets/start_background_base.png")


class GameBackground(Background):
    """ The default background which is used while playing."""
    def __init__(self):
        super().__init__(color=arcade.color.AMAZON)
