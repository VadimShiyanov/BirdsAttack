import pygame
pygame.init()

class Button:
    def __init__(self, image, image_hover, pos):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, screen, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.image_hover, self.rect.topleft)
            return True
        else:
            screen.blit(self.image, self.rect.topleft)
            return False
