from dataclasses import dataclass, field
from typing import Tuple

import arcade


@dataclass
class TextButton:
    x: int
    y: int
    width: int
    height: int
    text: str = field(default="")
    font_size: float = field(default=12.0)
    color: Tuple[int, int, int] = field(default=(255, 255, 255))
    text_color: Tuple[int, int, int] = field(default=(0, 0, 0))
    filled: bool = field(default=True)

    @property
    def left(self):
        return self.x - self.width / 2

    @property
    def right(self):
        return self.x + self.width / 2

    @property
    def top(self):
        return self.y + self.height / 2

    @property
    def bottom(self):
        return self.y - self.height / 2

    def draw(self):
        """ Draws the button."""
        drawfunc = (arcade.draw_lrtb_rectangle_filled if self.filled
                    else arcade.draw_lrtb_rectangle_outline)
        drawfunc(self.left, self.right, self.top, self.bottom, self.color)
        arcade.draw_text(self.text, self.x, self.y, self.text_color, self.font_size,
                         anchor_x="center", anchor_y="center")

    def is_inside(self, x, y) -> bool:
        """ Checks if the coordinates are inside the button."""
        return self.left < x < self.right and self.bottom < y < self.top
