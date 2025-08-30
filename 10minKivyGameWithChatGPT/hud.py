from kivy.uix.label import Label

class HUD(Label):
    """Heads-up display for lives, level, and score."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (1, 1, 1, 1)
        self.font_size = 20

    def update(self, player, level):
        self.text = f"Lives: {player.lives} | Level: {level} | Score: {player.score}"
