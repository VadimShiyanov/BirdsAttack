import pygame
import backend
from surce_loading import surce_loading
from Button import Button
from background import Background
from TextInputBox import TextInputBox

def register_screen(screen):
    assets = surce_loading()
    pygame.display.set_caption("Register Screen")
    pygame.display.set_icon(assets['icon'])

    font = assets['font']
    register_menu = Background(assets['register_menu'])

    button_register_in_reg = Button(assets['button_register_in_reg'], assets['button_register_in_reg_mouse'], (695, 690))
    button_back = Button(assets['button_back'], assets['button_back_mouse'], (100, 850))

    register_input_box = TextInputBox(720, 350, 140, 32, font, y_offset=-23)
    password_input_box = TextInputBox(735, 465, 140, 32, font, y_offset=-7)

    register_screen_running = True
    error_message = None

    while register_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            register_input_box.handle_event(event)
            password_input_box.handle_event(event)

        mouse = pygame.mouse.get_pos()
        register_menu.draw(screen)
        screen.blit(assets['register_string_1'], (725, 335))
        screen.blit(assets['register_string_2'], (735, 465))
        register_input_box.update()
        password_input_box.update()
        register_input_box.draw(screen)
        password_input_box.draw(screen)

        if button_register_in_reg.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                #password = password_input_box.text

                # ser reigister
                #if username and password:
                    #answer = backend.register(username, password)
                    #if answer:
                        #register_screen_running = False
                return 'menu'
                    #else:
                        #error_message = "Такой пользователь уже существует"

        if button_back.draw(screen, mouse):
            if pygame.mouse.get_pressed()[0]:
                register_screen_running = False
                return 'welcome'

        if error_message:
            error_text = font.render(error_message, True, (255, 0, 0))
            screen.blit(error_text, (720, 520))

        pygame.display.update()

    return True
