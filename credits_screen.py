import pygame
from Button import Button
from background import Background
from surce_loading import surce_loading

def credits(screen):
    pygame.init()
    assets = surce_loading()
    background_credits = Background(assets['bg_credits'])

    screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
    pygame.display.set_caption("Credits")
    pygame.display.set_icon(assets['icon'])


    credits_running = True
    while credits_running:
        button_back = Button(assets['button_back_mini'], assets['button_back_mouse_mini'], (1400, 800))
        mouse = pygame.mouse.get_pos()

        background_credits.draw(screen)

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                credits_running = False
                return 'menu'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'

        pygame.display.update()
