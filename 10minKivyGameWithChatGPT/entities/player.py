from kivy.properties import NumericProperty, BooleanProperty
from .entity import Entity
from config import PLAYER_JUMP_POWER

class Player(Entity):
    velocity_y = NumericProperty(0)
    lives = NumericProperty(2)
    score = NumericProperty(0)
    jump_power = NumericProperty(PLAYER_JUMP_POWER)
    on_ground = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__((0, 0, 1, 1), **kwargs)  # Blue

    def move(self, platforms):
        from config import GRAVITY
        self.velocity_y -= GRAVITY
        self.y += self.velocity_y

        landed = False
        for p in platforms:
            if self.collide_widget(p) and self.velocity_y <= 0:
                if self.y >= p.top - 20:
                    self.y = p.top
                    self.velocity_y = 0
                    self.on_ground = True
                    landed = True

        if self.y <= 0:
            self.y = 0
            self.velocity_y = 0
            self.on_ground = True
            landed = True

        if not landed:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False
