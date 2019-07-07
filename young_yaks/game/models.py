import arcade


class CowSpriteList(arcade.SpriteList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_pressed(self, x, y):
        for cow in self.sprite_list:
            cow.on_pressed(self, x, y)
