import arcade
import enum
import random

from . import constants


class CowBreed(enum.Enum):
    meat = 1
    milk = 2
    burp = 3

    def _resolve_image(self):
        if self.value == self.meat:
            return constants.MEAT_COW_IMAGE
        elif self.value == self.milk:
            return constants.MILK_COW_IMAGE
        elif self.value == self.burp:
            return constants.BURP_COW_IMAGE


class Cow(arcade.Sprite):
    def __init__(self, cow_breed: CowBreed, x: int, y: int):
        super().__init__("game/assets/cow.png", center_x=x, center_y=y)

        self.breed: CowBreed = cow_breed

        self.pressed: bool = False

    def update(self):
        super().update()
        if self.pressed is True:
            return

        if random.randint(0, 1000) == 0:
            self.strafe(1)
            self.strafe(-0.1)
            # self.change_x = random.choice([1, -1])

    def _is_inside(self, x, y):
        return self.left < x < self.right and self.bottom < y < self.top

    def on_pressed(self, x, y):
        if self._is_inside(x, y):
            self.pressed = True
        else:
            return

    def on_release(self, x, y):
        self.pressed = False

    def on_mouse_drag(self, x, y):
        self.center_x, self.center_y = x, y
