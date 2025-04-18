import pygame
from player import Player
from constants import *

def main():
    print("Starting Pong")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    
    drawable = pygame.sprite.Group()

    Player.containers = (drawable)

    #Instantiate players:
    player_1 = Player(PLAYER_1_POSITION_X, PLAYER_1_POSITION_Y, PLAYER_WIDTH, PLAYER_LENGTH) 
    player_2 = Player(PLAYER_2_POSITION_X, PLAYER_2_POSITION_Y, PLAYER_WIDTH, PLAYER_LENGTH) 


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


        
        

if __name__ == "__main__":
    main()