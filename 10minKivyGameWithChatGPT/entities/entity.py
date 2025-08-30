from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

class Entity(Widget):
    """Base class for all game objects (player, enemy, platform, coin)."""

    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
