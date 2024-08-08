import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background
from login_screen import login_screen
from register_screen import register_screen
from menu import main_menu
from end_screen import end_screen
from Game import game
from connection_lost_screen import connection_lost
import requests
import sys


def welcome():
    pygame.init()
    assets = surce_loading()

    screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
    pygame.display.set_caption("Welcome Screen")
    pygame.display.set_icon(assets['icon'])

    welcome_bg = Background(assets['welcome_bg'])
    button_login = Button(assets['button_login'], assets['button_login_mouse'], (700, 330))
    button_register = Button(assets['button_register'], assets['button_register_mouse'], (700, 480))

    current_screen = "welcome"  # Initial state

    while current_screen != "quit":
        if current_screen == "welcome":
            mouse = pygame.mouse.get_pos()
            welcome_bg.draw(screen)

            if button_login.draw(screen, mouse):
                if pygame.mouse.get_pressed()[0]:
                    current_screen = login_screen(screen)

            if button_register.draw(screen, mouse):
                if pygame.mouse.get_pressed()[0]:
                    current_screen = register_screen(screen)

        elif current_screen == "login":
            result = login_screen(screen)
            if result == "menu":
                current_screen = "menu"
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "register":
            result = register_screen(screen)
            if result == "menu":
                current_screen = "menu"
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "menu":
            result = main_menu(screen)
            if result == "play":
                current_screen = "play"
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "play":
            result = game(screen)
            if result == "end_screen":
                current_screen = "end_screen"

        elif current_screen == "end_screen":
            result = end_screen(screen)
            if result == "menu":
                current_screen = "menu"
            elif result == "play":
                current_screen = "play"

        try:
            pygame.display.update()
        except:
            pass

        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_screen = "quit"
        except:
            pass

def check_connection():
    try:
        response = requests.get("https://1.1.1.1")
        if response.status_code == 200:
            welcome()
        else:
            connection_lost()
    except requests.exceptions.ConnectionError:
        connection_lost()

check_connection()

pygame.quit()
sys.exit()