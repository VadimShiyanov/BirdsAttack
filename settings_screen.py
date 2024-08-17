import pygame
from sound_manager import SoundManager
from Button import Button
from background import Background
from surce_loading import surce_loading

def settings(screen, sound_manager):
    assets = surce_loading()
    pygame.display.set_caption("Settings")
    pygame.display.set_icon(assets['icon'])

    button_back = Button(assets['button_back'], assets['button_back_mouse'], (120, 800))
    

    sound_control_images = [
        pygame.image.load('images/settings_sound_control_panel_1.png'),
        pygame.image.load('images/settings_sound_control_panel_2.png'),
        pygame.image.load('images/settings_sound_control_panel_3.png'),
        pygame.image.load('images/settings_sound_control_panel_4.png'),
        pygame.image.load('images/settings_sound_control_panel_5.png')
    ]

    settings_sound_on = pygame.image.load('images/settings_sound_on.png')
    settings_sound_off = pygame.image.load('images/settings_sound_off.png')
    
    background_settings = Background(assets['background_settings'])


    rects = [
        pygame.Rect(900, 550, 34, 65),
        pygame.Rect(1045, 550, 34, 65),
        pygame.Rect(1200, 550, 34, 65),
        pygame.Rect(1350, 550, 34, 65),
        pygame.Rect(1570, 550, 34, 65)
    ]

    settings_running = True

    while settings_running:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, rect in enumerate(rects):
                    if rect.collidepoint(mouse):
                        # Устанавливаем громкость в зависимости от того, какой прямоугольник был нажат
                        sound_manager.set_volume((i + 1) * 0.2)
                        break
                

                sound_button_rect = pygame.Rect(1000, 295, settings_sound_on.get_width(), settings_sound_on.get_height())
                if sound_button_rect.collidepoint(mouse):
                    sound_manager.toggle_sound()

        background_settings.draw(screen)

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                settings_running = False
                return 'menu'


        if sound_manager.is_sound_on():
            current_volume_index = int(sound_manager.get_volume() / 0.2) - 1
            sound_control_image = sound_control_images[current_volume_index]
            screen.blit(sound_control_image, (900, 550))


        sound_button_image = settings_sound_on if sound_manager.is_sound_on() else settings_sound_off
        screen.blit(sound_button_image, (1000, 295))
        
        pygame.display.update()
