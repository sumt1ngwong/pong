import pygame

class RectShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, length):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()