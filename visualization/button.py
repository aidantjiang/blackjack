import pygame
from pygame.locals import *

pygame.font.init()

font_path = "public/fonts/sans-serif-bold.ttf"
font_size = 18

sans_serif_bold = pygame.font.Font(font_path, font_size)

DARK_BLUE = (43, 65, 98)
BLUE_GREY = (56, 95, 113)
OFF_WHITE = (245, 240, 246)
LIGHT_BROWN = (215, 179, 119)
DARK_BROWN = (143, 117, 79)

class Button:
    def __init__(self, x, y, width, height, text, action, font=sans_serif_bold):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = font
        self.visible = True

        #click effect
        self.default_color = (255,255,255)
        self.click_color = OFF_WHITE
        self.current_color = self.default_color
    def set_visibility(self, boolean):
        self.visible = boolean
    def draw(self, screen):
        if self.visible:  # Only draw the button if it's visible
            pygame.draw.rect(screen, self.current_color, self.rect)
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
    def handle_event(self, event):
        if self.visible:  # Handle events only if the button is visible
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.current_color = self.click_color
                    self.action()
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.current_color = self.default_color