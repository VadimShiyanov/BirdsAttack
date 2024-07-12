import pygame
from surce_loading import surce_loading

pygame.init()
clock = pygame.time.Clock()

assets = surce_loading()

screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")
pygame.display.set_icon(assets['icon'])

font = assets['font']
assets['background_music'].play()

running = True
bird_anim_count = 0

while running:
    clock.tick(12)
    screen.blit(assets['background'], (0, 0))
    screen.blit(assets['right_flight'][bird_anim_count], (960, 310))

    bird_anim_count = (bird_anim_count + 1) % 4  # Обновление счетчика анимации

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

assets['background_music'].stop()
pygame.quit()
