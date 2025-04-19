from rectshape import * 
from constants import *

class Ball(RectShape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y, width, length)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.length)
        self.velocity = pygame.Vector2(500, 600)

    def ball(self):
        #self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.length)
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.ball())

    def update(self, dt):        
        self.position += self.velocity * dt 
        
        if self.position.y <= 0 or self.position.y + self.length >= SCREEN_HEIGHT:
            self.velocity.y *= -1
        self.rect.topleft = self.position


    def rebound(self, dt):
        self.velocity.x *= -1
        self.position += self.velocity * dt 
        self.rect.topleft = self.position

        





