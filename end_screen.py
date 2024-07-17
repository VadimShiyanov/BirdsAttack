import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background
from Game import game

def end_screen(screen):
    assets = surce_loading()
    pygame.display.set_caption("End Screen")
    pygame.display.set_icon(assets['icon'])
    end_screen_bg = Background(assets['bg_end_screen'])
    button_replay = Button(assets['button_replay'], assets['button_replay_mouse'], (285, 690))
    button_main_menu = Button(assets['button_main_menu'], assets['button_main_menu_mouse'], (1170, 680))
    end_screen_running = True

    while end_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen_running = False
                return 'quit'
        
        mouse = pygame.mouse.get_pos()
        end_screen_bg.draw(screen)

        if button_replay.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                return 'play'

        if button_main_menu.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                return 'menu'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen_running = False
                pygame.quit()

        pygame.display.update()
