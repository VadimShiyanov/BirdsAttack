import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background
from login_screen import login_screen
from register_screen import register_screen
from menu import main_menu
from end_screen import end_screen
from Game import game
from Leaderbord_screen import leaderboard
from credits_screen import credits
from connection_lost_screen import connection_lost
from alt_loading_screen import show_image_centered
from settings_screen import settings
import alt_loading_screen
import sys
import backend
from sound_manager import SoundManager
import time
sound_manager = SoundManager()  
def welcome(sound_manager):
    pygame.init()
    assets = surce_loading()

    screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
    pygame.display.set_caption("Welcome Screen")
    pygame.display.set_icon(assets['icon'])

    welcome_bg = Background(assets['welcome_bg'])
    button_login = Button(assets['button_login'], assets['button_login_mouse'], (700, 330))
    button_register = Button(assets['button_register'], assets['button_register_mouse'], (700, 480))

    current_screen = "welcome"

    while current_screen != "quit":
        if current_screen == "welcome":
            mouse = pygame.mouse.get_pos()
            welcome_bg.draw(screen)

            if button_login.draw(screen, mouse):
                if pygame.mouse.get_pressed()[0]:
                    current_screen = login_screen(screen, sound_manager)

            if button_register.draw(screen, mouse):
                if pygame.mouse.get_pressed()[0]:
                    current_screen = register_screen(screen, sound_manager)

        elif current_screen == "login":
            result = login_screen(screen, sound_manager)
            if result == "menu":
                current_screen = "menu"
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "register":
            result = register_screen(screen, sound_manager)
            if result == "menu":
                current_screen = "menu"
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "menu":
            result = main_menu(screen, sound_manager)
            if result == "play":
                sound_manager.music_channel.stop()
                current_screen = "play"
            elif result == "settings":
                current_screen = settings(screen, sound_manager)
            elif result == "leaderboard":
                current_screen = leaderboard(screen)
            elif result == "credits":
                current_screen = credits(screen)
            elif result == "quit":
                current_screen = "quit"

        elif current_screen == "play":
            sound_manager.play_battle_music()
            result = game(screen, sound_manager)
            if result == "end_screen":
                sound_manager.stop_battle_music()
                current_screen = "end_screen"

        elif current_screen == "end_screen":
            result = end_screen(screen, sound_manager)
            sound_manager.play_end_music()
            if result == "menu":
                sound_manager.stop_end_music()
                if sound_manager.is_sound_on():
                    sound_manager.music_channel.play(sound_manager.menu_music, loops=-1)
                current_screen = "menu"
            elif result == "play":
                sound_manager.stop_end_music()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_screen = "quit"

def check_connection():
    result = backend.onetime_connection_check()
    if result:
        welcome(sound_manager)
    else:
        connection_lost()
    alt_loading_screen.root.destroy()

show_image_centered(check_connection)

pygame.quit()
sys.exit()
