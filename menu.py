import pygame
from surce_loading import surce_loading
from Button import Button
from background import Background

pygame.init()
assets = surce_loading()

screen_menu = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")
pygame.display.set_icon(assets['icon'])

# Создаем объекты фона и кнопок
background_menu = Background(assets['background_menu'])
button_play = Button(assets['button_play'], assets['button_play_mouse'], (700, 150))
button_leaderboard = Button(assets['button_leaderboard'], assets['button_leaderboard_mouse'], (700, 350))
button_settings = Button(assets['button_settings'], assets['button_settings_mouse'], (700, 550))
button_credits = Button(assets['button_credits'], assets['button_credits_mouse'], (700, 750))

running = True
running_menu = True

# Главное меню
while running_menu:
    mouse = pygame.mouse.get_pos()

    # Рисуем фон
    background_menu.draw(screen_menu)

    # Рисуем кнопки и проверяем нажатие
    if button_play.draw(screen_menu, mouse):
        if pygame.mouse.get_pressed()[0]:
            running_menu = False

    if button_leaderboard.draw(screen_menu, mouse):
        if pygame.mouse.get_pressed()[0]:
            running_menu = False

    if button_settings.draw(screen_menu, mouse):
        if pygame.mouse.get_pressed()[0]:
            running_menu = False

    if button_credits.draw(screen_menu, mouse):
        if pygame.mouse.get_pressed()[0]:
            running_menu = False

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_menu = False
            running = False

pygame.quit()
