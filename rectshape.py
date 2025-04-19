import pygame

class RectShape(pygame.sprite.Sprite):
    def __init__(self, x, y, width, length):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.width = width
        self.length = length
        self.position = pygame.Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.length)
        self.velocity = pygame.Vector2(0, 0)

    
    def draw(self, screen):
        pass 

    def update(self, dt):
        pass

    def check_collision(self, other_object):
        return self.rect.colliderect(other_object.rect)

     


    