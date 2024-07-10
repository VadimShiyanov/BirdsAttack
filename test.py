import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Niggers are pidors")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
