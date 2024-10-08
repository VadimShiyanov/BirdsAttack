import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background
import backend
from sound_manager import SoundManager

def main_menu(screen, sound_manager):
    assets = surce_loading()
    font = assets['font']
    pygame.display.set_caption("Main Menu")
    pygame.display.set_icon(assets['icon'])

    background_menu = Background(assets['background_menu'])
    button_play = Button(assets['button_play'], assets['button_play_mouse'], (700, 150))
    button_leaderboard = Button(assets['button_leaderboard'], assets['button_leaderboard_mouse'], (700, 350))
    button_settings = Button(assets['button_settings'], assets['button_settings_mouse'], (700, 550))
    button_credits = Button(assets['button_credits'], assets['button_credits_mouse'], (700, 750))

    if sound_manager.is_sound_on() and not sound_manager.music_channel.get_busy():
        sound_manager.music_channel.play(sound_manager.menu_music, loops=-1)

    running_menu = True

    while running_menu:
        mouse = pygame.mouse.get_pos()
        background_menu.draw(screen)
        
        nickname = backend.get_my_username()
        nickname_label = font.render(nickname, False, (0, 0, 0))
        screen.blit(nickname_label, (60, 75))

        if button_play.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                return 'play'

        if button_leaderboard.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                running_menu = False
                return 'leaderboard'

        if button_settings.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                running_menu = False
                return 'settings'

        if button_credits.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                running_menu = False
                return 'credits'

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_menu = False
                return 'quit'

    return 'quit'

