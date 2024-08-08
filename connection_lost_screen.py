import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background

def connection_lost():
    pygame.init()
    assets = surce_loading()
    screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
    pygame.display.set_caption("Connection Lost")
    pygame.display.set_icon(assets['icon'])

    connection_lost_screen_bg = Background(assets.get('connection_lost_screen'))

    button_ok = Button(assets.get('button_ok'), assets.get('button_ok_mouse'), (700, 740))

    running_connection_lost_screen = True

    while running_connection_lost_screen:
        mouse = pygame.mouse.get_pos()


        connection_lost_screen_bg.draw(screen)

        if button_ok.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                return False

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_connection_lost_screen = False
                pygame.quit()

    pygame.quit()
