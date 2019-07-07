import arcade


class CowSpriteList(arcade.SpriteList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_pressed(self, x, y):
        for cow in self.sprite_list:
            cow.on_pressed(x, y)

    def on_release(self, x, y):
        for cow in self.sprite_list:
            cow.on_release(x, y)
    
    def on_mouse_drag(self, x, y):
        for cow in self.sprite_list:
            if cow.pressed:
                cow.on_mouse_drag(x, y)
