import pygame
import random
import sys
pygame.init()

screen_height = 600
screen_width = 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))

world_height = screen_height//50
world_width = screen_width//50
world = []

class TileHUD:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pop = 0
        self.dev = 0



class Tile:
    def __init__(self, x, y):
        self.x = x * 50
        self.y = y * 50
        self.colour = GREEN

    def draw_tile(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, 50, 50))

    def select(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 50, 50), 1)

    def draw_hud(self):
        pygame.draw.rect(screen, WHITE, (self.x - 50, self.y - 50, 150, 50))

    def deselect(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, 50, 50), 1)

def world_init(world_height, world_width):
    for x in range(world_width):
        world.append([])
        for y in range(world_height):
            world[x].append(Tile(x, y))
            world[x][y].draw_tile()

def select_tile(coord):
    return world[coord[0]//50][coord[1]//50]

game_over = False
world_init(world_height, world_width)

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                selected_tile.deselect()
            except NameError:
                pass
            if event.button == 1:
                selected_tile = select_tile(event.pos)
                selected_tile.select()
                selected_tile.draw_hud()
        pygame.display.update()
