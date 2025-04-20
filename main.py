import pygame
import random
import sys
from player import *
from ball import *
from constants import *

def main():
    print("Starting Pong")
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_1_score = 0
    player_2_score = 0
    streak = 0
    last_streak_checkpoint = 0
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

        if ball.check_collision(player_1) or ball.check_collision(player_2):
            print("collide")
            ball.rebound(dt)
            streak += 1
        
        #Logic to make the game harder as streak increases
        if streak - last_streak_checkpoint >= 2:
            last_streak_checkpoint += 2
            ball.velocity += pygame.Vector2(50, 50)
            
        if ball.position.x >= SCREEN_WIDTH:
            player_1_score += 1 
            streak = 0
            ball.reset_ball()
            pygame.time.delay(1000)
        if ball.position.x + ball.width <= 0:
            player_2_score += 1 
            streak = 0 
            ball.reset_ball()
            pygame.time.delay(1000)

        font = pygame.font.Font(None, 36)
        score_text_player_1 = font.render(f'Score P1: {player_1_score}', True, (255, 255, 255))
        score_text_player_2 = font.render(f'Score P2: {player_2_score}', True, (255, 255, 255))
        streak_text = font.render(f'Streak: {streak}', True, (255, 255, 255))
        screen.blit(score_text_player_1, (10, 10))
        screen.blit(score_text_player_2, (1135, 10))
        screen.blit(streak_text, (580, 10))

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()