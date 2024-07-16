import pygame
import random

class Bird:
    def __init__(self, x, y, flight_images, speed):
        self.x = x
        self.y = y
        self.flight_images = flight_images
        self.speed = speed
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.anim_count = 0
        self.image = self.flight_images[self.direction][self.anim_count]

    def update(self):
        # Update position based on direction
        if self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

        self.anim_count = (self.anim_count + 1) % 4
        self.image = self.flight_images[self.direction][self.anim_count]

        # Check for screen boundaries and change direction
        if self.x < 0 or self.x > 1920 or self.y < 0 or self.y > 500:
            self.change_direction()

    def change_direction(self):
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.image = self.flight_images[self.direction][self.anim_count]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_hit(self, pos):
        return self.image.get_rect(topleft=(self.x, self.y)).collidepoint(pos)
    