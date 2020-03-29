import pygame, sys
from config import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True


    # run the game
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    # handle events from pygame
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        pygame.display.update()