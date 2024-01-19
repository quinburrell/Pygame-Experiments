import pygame
import random
import sys
pygame.init()

screen_height = 600
screen_width = 800

RED = (255,0,0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
player_pos = [400, 300]
player_size = 50
player_speed = 50
enemy_size = 50
enemy_pos = [random.randint(0,screen_width-enemy_size), 0]
enemy_speed = 10

screen = pygame.display.set_mode((screen_width, screen_height))

game_over = False

clock = pygame.time.Clock()


def collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and (p_x + player_size) >= e_x) or (e_x <= p_x and (e_x + enemy_size) >= p_x):
        if e_y == p_y:
            return True
    return False

while not game_over:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_speed
            elif event.key == pygame.K_UP:              
                player_pos[1] -= player_speed
            elif event.key == pygame.K_DOWN:
                player_pos[1] += player_speed            

    screen.fill(BLACK)
    if collision(player_pos, enemy_pos):
        game_over = True
        break
    if enemy_pos[1] >= 0 and enemy_pos[1] < screen_height:
        enemy_pos[1] += enemy_speed
    else:
        enemy_pos[0] = random.randint(0, screen_width-enemy_size)
        enemy_pos[1] = 0
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    
    clock.tick(30)
    pygame.display.update()
