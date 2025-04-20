import pygame 
from main import *
from constants import *
from rectshape import *

class Player(RectShape):
    def __init__(self, x, y, width, length, up_key, down_key):
        super().__init__(x, y, width, length)
        #below we need to make variables for movement as player 1 and 2 movement need to be independent
        self.up_key = up_key
        self.down_key = down_key
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.length)

    def paddle(self):
        #self.rect =  pygame.Rect(self.position.x, self.position.y, self.width, self.length)
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.paddle())

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[self.up_key] and self.position.y > 0:
            self.move(-dt)

        if keys[self.down_key] and self.position.y < SCREEN_HEIGHT - self.length :
            self.move(dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.topleft = self.position

