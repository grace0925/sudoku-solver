import pygame, sys
from config import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = BOARD
        print(BOARD)

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

    def drawGrid(self, window):
        # draw border
        pygame.draw.rect(window, BLACK, (GRID_POSITION[0], GRID_POSITION[1], GRID_WIDTH, GRID_HEIGHT), 2)
        # draw lines
        for x  in range(9):
            pygame.draw.line(window, BLACK, (GRID_POSITION[0], (x+1)*CELL_SIZE+GRID_POSITION[1]), (GRID_POSITION[0]+GRID_WIDTH, (x+1)*CELL_SIZE+GRID_POSITION[1]), 2)
            pygame.draw.line(window, BLACK, ((x+1)*CELL_SIZE+GRID_POSITION[0], GRID_POSITION[1]),((x+1)*CELL_SIZE+GRID_POSITION[0], GRID_POSITION[1]+GRID_HEIGHT), 2)



    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        pygame.display.update()