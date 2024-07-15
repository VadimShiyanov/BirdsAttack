import pygame
import random
from surce_loading import surce_loading
from Bird import Bird

pygame.init()
clock = pygame.time.Clock()

assets = surce_loading()

screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Game Menu")
pygame.display.set_icon(assets['icon'])

font = assets['font']
assets['background_music'].play(-1)

running = True
birds = []
bird_spawn_time = 1000  # Faster spawn time
last_bird_spawn = pygame.time.get_ticks()
bird_anim_count = 0
score = 0
ammo = 5
max_ammo = 5
ammo_reload_time = 3000
last_ammo_reload = pygame.time.get_ticks()

# Map flight directions to corresponding images
flight_images = {
    'left': assets['left_flight'],
    'right': assets['right_flight'],
    'up': assets['up_flight'],
    'down': assets['down_flight']
}

while running:
    clock.tick(60)
    screen.blit(assets['background'], (0, 0))

    # Spawn birds
    if len(birds) < 5 and pygame.time.get_ticks() - last_bird_spawn > bird_spawn_time:
        x = random.randint(0, 1920)
        y = random.randint(0, 500)
        speed = random.randint(5, 10)  # Increased speed
        direction = random.choice(['left', 'right', 'up', 'down'])
        birds.append(Bird(x, y, flight_images, speed))
        last_bird_spawn = pygame.time.get_ticks()

    # Update and draw birds
    for bird in birds:
        bird.update()
        bird.draw(screen)

    # Reload ammo
    if ammo < max_ammo and pygame.time.get_ticks() - last_ammo_reload > ammo_reload_time:
        ammo += 1
        last_ammo_reload = pygame.time.get_ticks()

    # Display score and ammo
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    ammo_text = font.render(f'Ammo: {ammo}', True, (255, 255, 255))
    screen.blit(score_text, (1600, 20))
    screen.blit(ammo_text, (1600, 80))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and ammo > 0:
            pos = pygame.mouse.get_pos()
            for bird in birds[:]:
                if bird.is_hit(pos):
                    birds.remove(bird)
                    score += 1
                    ammo -= 1

assets['background_music'].stop()
pygame.quit()
