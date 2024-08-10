import pygame
import backend
import time
from surce_loading import surce_loading
from Button import Button
from background import Background
from TextInputBox import TextInputBox

def login_screen(screen):
    assets = surce_loading()

    pygame.display.set_caption("Login Screen")
    pygame.display.set_icon(assets['icon'])

    font = assets['font']
    login_menu = Background(assets['login_menu'])
    button_login_in_reg = Button(assets['button_login_in_reg'], assets['button_login_in_reg_mouse'], (695, 690))
    button_back = Button(assets['button_back'], assets['button_back_mouse'], (100, 850))

    login_input_box = TextInputBox(720, 350, 140, 32, font, y_offset=-7)
    password_input_box = TextInputBox(735, 465, 140, 32, font, y_offset=-7)

    login_menu_error_code = (assets['login_menu_error_code'])

    def enter_log_error_code():
        screen.blit(login_menu_error_code, (0, 0))
        pygame.display.update()
        time.sleep(3)


    login_screen_running = True

    while login_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            login_input_box.handle_event(event)
            password_input_box.handle_event(event)

        mouse = pygame.mouse.get_pos()
        login_menu.draw(screen)
        screen.blit(assets['login_string_1'], (720, 350))
        screen.blit(assets['login_string_2'], (735, 465))
        login_input_box.update()
        password_input_box.update()
        login_input_box.draw(screen)
        password_input_box.draw(screen)

        if button_login_in_reg.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                password = password_input_box.text
                username = login_input_box.text
                try:
                    auth = backend.login(username, password)
                    can_continue = True
                except:
                    can_continue = False
                    print("Тут должна быть картинка что логин или пароль не может быть пустым текстом и / или недолжен содержать знак ;")
                if can_continue:
                    if auth == True:
                        login_screen_running = False
                        return 'menu'
                    else:
                        enter_log_error_code()

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                login_screen_running = False
                return 'welcome'

        pygame.display.update()

    return True
