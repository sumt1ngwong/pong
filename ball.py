from rectshape import * 

class Ball(RectShape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y, width, length)

    def ball(self):
        return pygame.Rect(self.position.x, self.position.y, self.width, self.length)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.ball())

    def update(self, dt):
        pass



