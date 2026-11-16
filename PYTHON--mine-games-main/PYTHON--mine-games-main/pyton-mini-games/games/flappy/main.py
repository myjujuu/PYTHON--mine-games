import pygame
import random
import os 

from common.colors import *
from common.constants import *
from common.ui import draw_score, draw_start_msg

def run_snake(screen):

    clock = pygame.time.Clock()

    base = os.path.abspath(os.path.join(os.path.dirname(_file_), "../../assets/snake"))

    bg = pygame.image.load(os.path.join(base, "bg.png"))
    bg = pygame.transform.scale(bg,(width, height))

    obstacle_img = pygame.image.load(os.path.join(base, "obstacle.png"))
    obstacle_img = pygame.transform.scale(obstacle_img,(10,10))

    snake = [(100,100)]
    dx,dy = 10,0

    grid = 10

    obstacles = []
    while len(obstacles) < 25:
        pos = (
            random.randrange(20,width-20,grid),
            random.randrange(20,height-20,grid)
        )
        if pos not in snake:
            obstacles.append(pos)

    def place_food():
        while True:
            candidate = (
                random.randrange(20,width-20,grid),
                random.randrange(20,height-20,grid)
            )
            if candidate not in snake and candidate not in obstacles:
                return candidate

    food = place_food()

    speed = 8
    score = 0
    started = False
    paused = False

    running = True
    while running:
        screen.blit(bg,(0,0))

        panel = pygame.Surface((width-40, height-40), pygame.SRCALPHA)
        panel.fill((*BG_PANEL, 190))
        pygame.draw.rect(panel, (*BG_PANEL_LIGHT, 220), panel.get_rect(), border_radius=16, width=2)
        screen.blit(panel, (20,20))

        for x in range(20, width-20, grid):
            pygame.draw.line(screen, (*BG_SOFT, 40), (x,20), (x,height-20), 1)
        for y in range(20, height-20, grid):
            pygame.draw.line(screen, (*BG_SOFT, 40), (20,y), (width-20,y),1)

        for o in obstacles:
            screen.blit(obstacle_img,o)

        food center = (food[0] + 5, food[1] + 5)
        