import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background

def settings(screen):
    assets = surce_loading()
    pygame.display.set_caption("Settings")
    pygame.display.set_icon(assets['icon'])
    
    button_back = Button(assets['button_back'], assets['button_back_mouse'], (120, 800))
    background_settings = Background(assets['background_settings'])

    settings_running = True
    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
                return 'quit'
        
        mouse = pygame.mouse.get_pos()
        background_settings.draw(screen)

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                settings_running = False
                return 'menu'

        pygame.display.update()
