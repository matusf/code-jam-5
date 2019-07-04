import arcade


class Background:
    """ A class representing a window background."""
    def __init__(self, texture=None, color=None):
        self.texture = texture
        # We don't allow both attributes at the same time
        self.colour = color if texture is None else None

    def draw(self):
        if self.texture:
            arcade.draw_texture_rectangle(320/2, 180/2, 320, 180, self.texture)
        else:
            arcade.draw_rectangle_filled(320/2, 180/2, 320, 180, arcade.color.AMAZON)


class StartBackground(Background):
    """ The background you start with, this inherits from Background."""
    def __init__(self):
        super().__init__(color=arcade.color.AMAZON)
