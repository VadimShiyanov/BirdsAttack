import pygame
import random
import backend
from surce_loading import surce_loading
from Bird import Bird

def game(screen, sound_manager):
    pygame.init()
    clock = pygame.time.Clock()

    assets = surce_loading()
    pygame.display.set_caption("Game Menu")
    pygame.display.set_icon(assets['icon'])

    font = assets['font']
    sound_manager.play_battle_music()  # Воспроизведение музыки битвы

    running = True
    birds = []
    bird_spawn_time = 1000
    last_bird_spawn = pygame.time.get_ticks()
    score = 0
    ammo = 5
    max_ammo = 5
    ammo_reload_time = 1500
    last_ammo_reload = pygame.time.get_ticks()
    start_time = pygame.time.get_ticks()
    game_duration = 60000  # 60 секунд

    flight_images = {
        'left': assets['left_flight'],
        'right': assets['right_flight'],
        'up': assets['up_flight'],
        'down': assets['down_flight']
    }

    while running:
        clock.tick(60)

        screen.blit(assets['background'], (0, 0))

        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time >= game_duration:
            birds.clear()
            sound_manager.stop_battle_music()  # Остановите музыку битвы
            backend.save_score_local(score)
            running = False
            return 'end_screen'

        remaining_time = (game_duration - elapsed_time) // 1000
        timer_text = font.render(f'Time: {remaining_time}', True, (255, 255, 255))
        screen.blit(timer_text, (1700, 20))

        if len(birds) < 10 and pygame.time.get_ticks() - last_bird_spawn > bird_spawn_time:
            x = random.randint(0, screen.get_width())
            y = random.randint(0, 500)
            speed = random.randint(10, 20)
            birds.append(Bird(x, y, flight_images, speed))
            last_bird_spawn = pygame.time.get_ticks()

        for bird in birds:
            bird.update()
            bird.draw(screen)

        # Перезарядка
        if ammo < max_ammo and pygame.time.get_ticks() - last_ammo_reload > ammo_reload_time:
            ammo += 1
            last_ammo_reload = pygame.time.get_ticks()

        # Отображение счета и боеприпасов
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        ammo_text = font.render(f'Ammo: {ammo}', True, (255, 255, 255))
        screen.blit(score_text, (1600, 80))
        screen.blit(ammo_text, (1600, 140))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sound_manager.stop_battle_music()  # Остановите музыку битвы
                running = False
                pygame.quit()
                return 'quit'

            elif event.type == pygame.MOUSEBUTTONDOWN and ammo > 0:
                pos = pygame.mouse.get_pos()
                hit = False  # Флаг попадания

                # Проверка попадания по птицам
                for bird in birds[:]:
                    if bird.is_hit(pos):
                        birds.remove(bird)
                        score += 1
                        hit = True  # Устанавливаем флаг, если попали в птицу

                # Расходуем патрон независимо от того, попали или нет
                ammo -= 1

    return 'end_screen'
