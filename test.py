import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1030), flags=pygame.RESIZABLE)
pygame.display.set_caption("Niggers are pidors")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
running = True
font = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 50)
background = pygame.image.load('images/backimg.png')
up_flight = [pygame.image.load('images/bird_animation/bird1_up.png'),
             pygame.image.load('images/bird_animation/bird2_up.png'),
             pygame.image.load('images/bird_animation/bird3_up.png'),
             pygame.image.load('images/bird_animation/bird4_up.png')]

down_flight = [pygame.image.load('images/bird_animation/bird1_down.png'),
               pygame.image.load('images/bird_animation/bird2_down.png'),
               pygame.image.load('images/bird_animation/bird3_down.png'),
               pygame.image.load('images/bird_animation/bird4_down.png')]

right_flight = [pygame.image.load('images/bird_animation/bird1_right.png'),
                pygame.image.load('images/bird_animation/bird2_right.png'),
                pygame.image.load('images/bird_animation/bird3_right.png'),
                pygame.image.load('images/bird_animation/bird4_right.png')]
left_right = [pygame.image.load('images/bird_animation/bird1_left.png'),
              pygame.image.load('images/bird_animation/bird2_left.png'),
              pygame.image.load('images/bird_animation/bird3_left.png'),
              pygame.image.load('images/bird_animation/bird4_left.png')]
background_music = pygame.mixer.Sound('music/battle1.mp3')
background_music.play()

bird_anim_count = 0
while running:
    clock.tick(12)
    screen.blit(background, (0, 0))
    screen.blit(right_flight[bird_anim_count],(960, 310))
    if bird_anim_count == 3:
        bird_anim_count = 0
    else:
        bird_anim_count += 1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()