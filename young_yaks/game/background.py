import arcade


class Background:
    """ A class representing a window background."""
    def __init__(self, texture=None, color=None):
        self.texture = texture
        # Here's why this class isn't a dataclass
        if texture is None:
            self.color = color
        else:
            raise UserWarning("`texture` and `color` cannot be set at the same time")

    def draw(self):
        if self.texture:
            arcade.draw_texture_rectangle(320/2, 180/2, 320, 180, self.texture)
        else:
            arcade.draw_rectangle_filled(320/2, 180/2, 320, 180, arcade.color.AMAZON)
