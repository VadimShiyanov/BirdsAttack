import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background
from login_screen import login_screen
from menu import main_menu

pygame.init()
assets = surce_loading()

screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Welcome Screen")
pygame.display.set_icon(assets['icon'])

welcome_bg = Background(assets['welcome_bg'])
button_login = Button(assets['button_login'], assets['button_login_mouse'], (700, 330))
button_register = Button(assets['button_register'], assets['button_register_mouse'], (700, 480))

running = True

while running:
    welcome_screen_running = True
    while welcome_screen_running:
        mouse = pygame.mouse.get_pos()
        welcome_bg.draw(screen)

        if button_login.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                welcome_screen_running = False
                next_screen = login_screen(screen)
                if next_screen == 'quit':
                    running = False
                elif next_screen == 'menu':
                    if not main_menu(screen) == 'quit':
                        running = False

        if button_register.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                welcome_screen_running = False
                running = False  # Exit the program

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                welcome_screen_running = False
                running = False

pygame.quit()
