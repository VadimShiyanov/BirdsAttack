import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Niggers are pidors")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
running = True
font = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 50)
while running:
    color_first = random.randint(0, 255)
    color_second = random.randint(0, 255)
    color_third = random.randint(0, 255)
    test_text = font.render("Niggers are pidors!", True, (color_first, color_second, color_third))
    screen.blit(test_text, (960, 515))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                screen.fill((color_first, color_second, color_third))
                pygame.display.update()