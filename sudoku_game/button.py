import pygame
from sudoku_game.config import *


class Button:
    def __init__(self, x, y, width, height, text=None, color=LIGHT_GREEN, highlightedColour=DARK_GREEN, function=None,
                 params=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.colour = color
        self.highlightedColour = highlightedColour
        self.function = function
        self.params = params
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(self.highlightedColour if self.highlighted else self.colour)
        window.blit(self.image, self.pos)
