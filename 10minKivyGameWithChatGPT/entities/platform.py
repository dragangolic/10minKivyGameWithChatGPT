from .entity import Entity

class Platform(Entity):
    def __init__(self, **kwargs):
        super().__init__((0.55, 0.27, 0.07, 1), **kwargs)  # Brown
