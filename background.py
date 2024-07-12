import pygame

class Background:
    def __init__(self, image, pos=(0, 0)):
        self.image = image
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)
