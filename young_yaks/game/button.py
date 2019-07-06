import arcade


class Button:
    """ A pressable button """
    def __init__(self, center_x, center_y,
                 width, height,
                 text, font="Arial", font_size=18,
                 font_color=arcade.color.BLACK,
                 color=arcade.color.LIGHT_GRAY,
                 pressed_color=arcade.color.DARK_GRAY,
                 button_height=1):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.color = color
        self.pressed_color = pressed_color
        self.button_height = 1
        self.pressed = False

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.color)
        arcade.draw_text(self.text, self.center_x, self.center_y,
                         self.font_color, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        pass

    def on_release(self):
        pass


class ActionButton(Button):
    """ Action-based button """
    def __init__(self, *, action, **kwargs):
        super().__init__(**kwargs)

        self.action = action

    def on_release(self):
        self.action()
