import pygame
from player import *
from ball import *
from constants import *

def main():
    print("Starting Pong")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Ball.containers = (drawable, updatable)

    #Instantiate players:
    player_1 = Player(PLAYER_1_POSITION_X, PLAYER_1_POSITION_Y, PLAYER_WIDTH, PLAYER_LENGTH, pygame.K_w, pygame.K_s) 
    player_2 = Player(PLAYER_2_POSITION_X, PLAYER_2_POSITION_Y, PLAYER_WIDTH, PLAYER_LENGTH, pygame.K_UP, pygame.K_DOWN) 

    #Instantiate Ball:
    ball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, BALL_WIDTH, BALL_LENGTH)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        updatable.update(dt)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


        
        

if __name__ == "__main__":
    main()