import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background

def login_screen(screen):
    assets = surce_loading()

    pygame.display.set_caption("Login Screen")
    pygame.display.set_icon(assets['icon'])

    login_menu = Background(assets['login_menu'])
    button_login_in_reg = Button(assets['button_login_in_reg'], assets['button_login_in_reg_mouse'], (695, 690))
    button_back = Button(assets['button_back'], assets['button_back_mouse'], (100, 850))

    login_screen_running = True

    while login_screen_running:
        mouse = pygame.mouse.get_pos()
        login_menu.draw(screen)

        if button_login_in_reg.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                login_screen_running = False
                return 'menu'

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                login_screen_running = False
                return 'welcome'

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login_screen_running = False
                return False  # Indicates that the game should quit

    return True  # Indicates that the game should continue to the next screen
