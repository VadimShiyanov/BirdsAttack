import pygame
import time

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_on = True
        

        self.menu_music = pygame.mixer.Sound('music/menu.mp3')
        self.battle_music = pygame.mixer.Sound('music/battle.mp3')
        self.end_music = pygame.mixer.Sound('music/end.mp3')


        self.music_channel = pygame.mixer.Channel(0)
        self.battle_channel = pygame.mixer.Channel(1)
        self.end_channel = pygame.mixer.Channel(2)

        self.volume = 1.0
        self.set_volume(self.volume)

        if self.sound_on:
            self.music_channel.play(self.menu_music, loops=-1)

    def toggle_sound(self):
        self.sound_on = not self.sound_on
        if self.sound_on:
            self.music_channel.play(self.menu_music, loops=-1)
        else:
            self.stop_all_music()

    def is_sound_on(self):
        return self.sound_on

    def play_battle_music(self):
        if self.sound_on:
            self.battle_channel.play(self.battle_music, loops=-1)

    def play_end_music(self):
        if self.sound_on:
            time.sleep(5)
            self.end_channel.play(self.end_music, loops=0)
            

    def stop_battle_music(self):
        self.battle_channel.stop()

    def stop_end_music(self):
        self.end_channel.stop()

    def stop_menu_music(self):  
        self.music_channel.stop()

    def stop_all_music(self):
        self.music_channel.stop()
        self.battle_channel.stop()
        self.end_channel.stop()


    def set_volume(self, volume):
        """ Устанавливает уровень громкости на всех каналах. """
        self.volume = max(0.0, min(1.0, volume))
        self.music_channel.set_volume(self.volume)
        self.battle_channel.set_volume(self.volume)
        self.end_channel.set_volume(self.volume)

    def increase_volume(self):
        """ Увеличивает громкость на 20%. """
        new_volume = self.volume + 0.2
        self.set_volume(new_volume)

    def decrease_volume(self):
        """ Уменьшает громкость на 20%. """
        new_volume = self.volume - 0.2
        self.set_volume(new_volume)

    def get_volume(self):
        return self.volume
