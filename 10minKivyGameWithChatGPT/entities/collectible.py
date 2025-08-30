from .entity import Entity

class Collectible(Entity):
    def __init__(self, **kwargs):
        super().__init__((1, 1, 0, 1), **kwargs)  # Yellow coin

