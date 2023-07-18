import pygame
from pygame.locals import *

pygame.font.init()

font_path = "public/fonts/sans-serif-bold.ttf"
font_size = 18

sans_serif_bold = pygame.font.Font(font_path, font_size)

class Button:
    def __init__(self, x, y, width, height, text, action, font=sans_serif_bold):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = font
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()