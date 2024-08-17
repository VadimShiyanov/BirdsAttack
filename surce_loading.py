import pygame
def surce_loading():
    # images
    icon = pygame.image.load('images/icon.png')
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

    left_flight = [pygame.image.load('images/bird_animation/bird1_left.png'),
                   pygame.image.load('images/bird_animation/bird2_left.png'),
                   pygame.image.load('images/bird_animation/bird3_left.png'),
                   pygame.image.load('images/bird_animation/bird4_left.png')]

    background_menu = pygame.image.load('images/bg_menu.png')
    background_welcome = pygame.image.load('images/welcome_bg.png')
    welcome_bg = pygame.image.load('images/welcome_bg.png')
    login_menu  = pygame.image.load('images/login_menu.png')
    connection_lost_screen = pygame.image.load('images/connection_lost_screen.png')
    register_menu = pygame.image.load('images/register_menu.png')
    bg_end_screen = pygame.image.load('images/bg_end_screen.png')
    background_settings = pygame.image.load('images/bg_settings.png')
    login_string_1 = pygame.image.load('images/login_string_1.png')
    login_string_2 = pygame.image.load('images/login_string_2.png')
    register_string_1 = pygame.image.load('images/register_string_1.png')
    register_string_2 = pygame.image.load('images/register_string_2.png')
    button_main_menu = pygame.image.load('images/button_main_menu.png')
    button_main_menu_mouse = pygame.image.load('images/button_main_menu_mouse.png')
    button_replay = pygame.image.load('images/button_replay.png')
    button_replay_mouse = pygame.image.load('images/button_replay_mouse.png')
    button_login_in_reg = pygame.image.load('images/button_login_in_reg.png')
    button_login_in_reg_mouse = pygame.image.load('images/button_login_in_reg_mouse.png')
    button_register_in_reg = pygame.image.load('images/button_register_in_reg.png')
    button_register_in_reg_mouse = pygame.image.load('images/button_register_in_reg_mouse.png')
    button_login = pygame.image.load('images/button_login.png')
    button_login_mouse = pygame.image.load('images/button_login_mouse.png')
    button_register = pygame.image.load('images/button_register.png')
    button_register_mouse = pygame.image.load('images/button_register_mouse.png')
    button_play = pygame.image.load('images/button_play.png')
    button_play_mouse = pygame.image.load('images/button_play_mouse.png')
    button_leaderboard = pygame.image.load('images/button_leaderboard.png')
    button_leaderboard_mouse = pygame.image.load('images/button_leaderboard_mouse.png')
    button_settings = pygame.image.load('images/button_settings.png')
    button_settings_mouse = pygame.image.load('images/button_settings_mouse.png')
    button_credits = pygame.image.load('images/button_credits.png')
    button_credits_mouse = pygame.image.load('images/button_credits_mouse.png')
    button_back = pygame.image.load('images/button_back.png')
    button_back_mouse = pygame.image.load('images/button_back_mouse.png')
    button_ok = pygame.image.load('images/button_ok.png')
    button_ok_mouse = pygame.image.load('images/button_ok_mouse.png')
    leaderboard_1 = pygame.image.load('images/leaderboard_1.png')
    leaderboard_2 = pygame.image.load('images/leaderboard_2.png')
    leaderboard_3 = pygame.image.load('images/leaderboard_3.png')
    leaderboard_4 = pygame.image.load('images/leaderboard_4.png')
    settings_sound_on = pygame.image.load('images/settings_sound_on.png')
    settings_sound_off = pygame.image.load('images/settings_sound_off.png')
    settings_sound_control_panel_1 = pygame.image.load('images/settings_sound_control_panel_1.png')
    settings_sound_control_panel_2 = pygame.image.load('images/settings_sound_control_panel_2.png')
    settings_sound_control_panel_3 = pygame.image.load('images/settings_sound_control_panel_3.png')
    settings_sound_control_panel_4 = pygame.image.load('images/settings_sound_control_panel_4.png')
    settings_sound_control_panel_5 = pygame.image.load('images/settings_sound_control_panel_5.png')
    register_menu_error_code = pygame.image.load('images/register_menu_error_code.png')
    login_menu_error_code = pygame.image.load('images/login_menu_error_code.png')
    register_menu_error_code_2 = pygame.image.load('images/register_menu_error_code_2.png')
    login_menu_error_code_2 = pygame.image.load('images/login_menu_error_code_2.png')
    # fonts
    font = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 50)
    font1 = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 75)
    font2 = pygame.font.Font('fonts/Roboto-BlackItalic.ttf', 100)

    # music
    battle_music = pygame.mixer.Sound('music/battle.mp3')
    end_music = pygame.mixer.Sound('music/end.mp3')
    menu_music = pygame.mixer.Sound('music/menu.mp3')

    return {
        'icon': icon,
        'background': background,
        'background_welcome': background_welcome,
        'background_menu': background_menu,
        'background_settings': background_settings,
        'login_string_1': login_string_1,
        'login_string_2': login_string_2,
        'register_string_1': register_string_1,
        'register_string_2': register_string_2,
        'welcome_bg': welcome_bg,
        'connection_lost_screen': connection_lost_screen,
        'bg_end_screen': bg_end_screen,
        'login_menu': login_menu,
        'register_menu': register_menu,
        'button_main_menu': button_main_menu,
        'button_main_menu_mouse': button_main_menu_mouse,
        'button_replay': button_replay,
        'button_replay_mouse': button_replay_mouse,
        'button_login_in_reg': button_login_in_reg,
        'button_login_in_reg_mouse': button_login_in_reg_mouse,
        'button_register_in_reg': button_register_in_reg,
        'button_register_in_reg_mouse': button_register_in_reg_mouse,
        'button_ok': button_ok,
        'button_ok_mouse': button_ok_mouse,
        'leaderboard_1': leaderboard_1,
        'leaderboard_2': leaderboard_2,
        'leaderboard_3': leaderboard_3,
        'leaderboard_4': leaderboard_4,
        'up_flight': up_flight,
        'down_flight': down_flight,
        'right_flight': right_flight,
        'left_flight': left_flight,
        'button_play': button_play,
        'button_login': button_login,
        'button_login_mouse': button_login_mouse,
        'button_register': button_register,
        'button_register_mouse': button_register_mouse,
        'button_play_mouse': button_play_mouse,
        'button_leaderboard': button_leaderboard,
        'button_leaderboard_mouse': button_leaderboard_mouse,
        'button_settings': button_settings,
        'button_settings_mouse': button_settings_mouse,
        'button_credits': button_credits,
        'button_credits_mouse': button_credits_mouse,
        'button_back': button_back,
        'button_back_mouse': button_back_mouse,
        'settings_sound_on': settings_sound_on,
        'settings_sound_off': settings_sound_off,
        'settings_sound_control_panel_1': settings_sound_control_panel_1,
        'settings_sound_control_panel_2': settings_sound_control_panel_2,
        'settings_sound_control_panel_3': settings_sound_control_panel_3,
        'settings_sound_control_panel_4': settings_sound_control_panel_4,
        'settings_sound_control_panel_5': settings_sound_control_panel_5,
        'register_menu_error_code': register_menu_error_code,
        'login_menu_error_code': login_menu_error_code,
        'register_menu_error_code_2': register_menu_error_code_2,
        'login_menu_error_code_2': login_menu_error_code_2,
        'font': font,
        'font1': font1,
        'font2': font2,
        'battle_music': battle_music,
        'end_music': end_music,
        'menu_music': menu_music
    }
