import pygame

class TextInputBox:
    def __init__(self, x, y, w, h, font, y_offset=-2, max_length=20, text_color=pygame.Color('black')):
        self.rect = pygame.Rect(x, y, w * 10, h)
        self.text_color = text_color
        self.text = ''
        self.font = font
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.active = False
        self.max_length = max_length
        self.y_offset = y_offset

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.max_length:
                        self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.text_color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width * 5

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + self.y_offset)) 
