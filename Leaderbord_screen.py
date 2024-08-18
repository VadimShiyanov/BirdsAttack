import pygame
from Button import Button
from background import Background
from surce_loading import surce_loading
import backend

def leaderboard(screen):
    assets = surce_loading()
    pygame.display.set_caption("Leaderboard")
    pygame.display.set_icon(assets['icon'])

    button_back = Button(assets['button_back_mini'], assets['button_back_mouse_mini'], (25, 800))
    
    scores = backend.all_scores()
    
    sorted_scores = sorted(scores.items(), key=lambda item: int(item[1]), reverse=True)
    
    backgrounds = [
        Background(assets['leaderboard_1']),
        Background(assets['leaderboard_2']),
        Background(assets['leaderboard_3']),
        Background(assets['leaderboard_4'])
    ]
    
    players_per_page = 20
    current_page = 0       
    total_pages = (len(sorted_scores) - 1) // players_per_page + 1

    leaderboard_running = True
    while leaderboard_running:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            

        # Выбор фона в зависимости от текущей страницы
        if current_page < len(backgrounds):
            backgrounds[current_page].draw(screen)
        else:
            backgrounds[-1].draw(screen)

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                leaderboard_running = False
                return 'menu'

        start_index = current_page * players_per_page
        end_index = start_index + players_per_page
        

        font = pygame.font.Font(None, 85)
        
        for i, (username, score) in enumerate(sorted_scores[start_index:end_index]):
            username_text = font.render(f"{i + 1 + start_index}. {username}", True, (255, 255, 255))
            score_text = font.render(f"{score}", True, (255, 255, 255))
            
            screen.blit(username_text, (330, 250 + i * 70))
            screen.blit(score_text, (1340, 250 + i * 70))

        pygame.display.update()
