import pygame, sys
from config import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = BOARD
        self.selected = None
        self.mousePos = None

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouse_clicked()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None

    def mouse_clicked(self):
        if self.mousePos[0] < GRID_POSITION[0] or self.mousePos[0] > GRID_POSITION[0] + GRID_WIDTH:
            return False
        if self.mousePos[1] < GRID_POSITION[1] or self.mousePos[1] > GRID_POSITION[1] + GRID_HEIGHT:
            return False
        return (self.mousePos[1] - GRID_POSITION[1])//CELL_SIZE, (self.mousePos[0] - GRID_POSITION[0])//CELL_SIZE

    def draw_grid(self, window):
        # draw border
        pygame.draw.rect(window, BLACK, (GRID_POSITION[0], GRID_POSITION[1], GRID_WIDTH, GRID_HEIGHT), 4)
        # draw lines
        for x in range(1, 10):
            if x % 3:
                line_weight = 1
            else:
                line_weight = 4
            pygame.draw.line(window, BLACK, (x * CELL_SIZE + GRID_POSITION[0], GRID_POSITION[1]),
                             (x * CELL_SIZE + GRID_POSITION[0], GRID_POSITION[1] + GRID_HEIGHT), line_weight)

            pygame.draw.line(window, BLACK, (GRID_POSITION[0], x * CELL_SIZE + GRID_POSITION[1]),
                             (GRID_POSITION[0] + GRID_WIDTH, x * CELL_SIZE + GRID_POSITION[1]), line_weight)

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def draw_selected_cell(self, window, selected_pos):
        pygame.draw.rect(window, GREEN, (selected_pos[1]*CELL_SIZE+GRID_POSITION[0], selected_pos[0]*CELL_SIZE+GRID_POSITION[1], CELL_SIZE, CELL_SIZE))

    def draw(self):
        self.window.fill(WHITE)
        if self.selected:
            self.draw_selected_cell(self.window, self.selected)
        self.draw_grid(self.window)
        pygame.display.update()