
import pygame
import random
from pygame.rect import Rect
from settings import Settings
from Block import Block


class Environment():
    def __init__(self, screen, num_ini_blocks):
        self.blocks = []
        self.num_ini_blocks = num_ini_blocks
        self.color_fondo = (255,0,0)
    def movement_blocks(self):
        for block in self.blocks:
            block.movement_block(-5,0)

    def cambio_fondo(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_t]:
            self.color_fondo = (0,0,255)
        if self.keys[pygame.K_y]:
            self.color_fondo = (255,0,0)

    def generate_blocks(self,y):
        sum = 0
        color_name = ""
        for i in range(0,self.num_ini_blocks):
            if random.randint(0, 1) == 0: 
                color_name = (0,0,255)
            else:
                color_name = (255,0,0)
            self.blocks.append(Block(random.randint(0,100) + sum, y+random.randint(-200,200), 100, 40, color_name))
            sum += 400
    
    def check_collisions(self):
        pass

    def blitall(self, screen):
        screen.fill(self.color_fondo)
        for block in self.blocks:
            block.blitme(screen)
    