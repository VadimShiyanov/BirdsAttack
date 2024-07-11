import pygame
pygame.init()
screen_menu = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Niggers are pidors")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
running = True
background = pygame.image.load('images/bg_menu.png')
button_play = pygame.image.load('images/button_play.png')
button_play_mouse = pygame.image.load('images/button_play_mouse.png')
button_leaderboard = pygame.image.load('images/button_leaderboard.png')
button_leaderboard_mouse = pygame.image.load('images/button_leaderboard_mouse.png')
button_settings = pygame.image.load('images/button_settings.png')
button_settings_mouse = pygame.image.load('images/button_settings_mouse.png')
button_credits = pygame.image.load('images/button_credits.png')
button_credits_mouse = pygame.image.load('images/button_credits_mouse.png')
button_play_rect = button_play.get_rect(topleft=(700, 150))
button_leaderboard_rect = button_leaderboard.get_rect(topleft=(700, 350))
button_settings_rect = button_settings.get_rect(topleft=(700, 550))
button_credits_rect = button_credits.get_rect(topleft=(700, 750))


while running:
    mouse = pygame.mouse.get_pos()
    screen_menu.blit(background, (0, 0))
    if button_play_rect.collidepoint(mouse):
        screen_menu.blit(button_play_mouse, (700, 150))
    else:
        screen_menu.blit(button_play, (700, 150))
    
    if button_leaderboard_rect.collidepoint(mouse):
        screen_menu.blit(button_leaderboard_mouse, (700, 350))
    else:
        screen_menu.blit(button_leaderboard, (700, 350))
    
    if button_settings_rect.collidepoint(mouse):
        screen_menu.blit(button_settings_mouse, (700, 550))
    else:
        screen_menu.blit(button_settings, (700, 550))
    
    if button_credits_rect.collidepoint(mouse):
        screen_menu.blit(button_credits_mouse, (700, 750))
    else:
        screen_menu.blit(button_credits, (700, 750))
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()