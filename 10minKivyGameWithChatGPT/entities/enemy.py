from kivy.core.window import Window
from .entity import Entity
from config import ENEMY_SPEED

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__((1, 0, 0, 1), **kwargs)  # Red
        self.direction = 1

    def move(self):
        self.x += self.direction * ENEMY_SPEED
        if self.x < 0 or self.right > Window.width:
            self.direction *= -1
