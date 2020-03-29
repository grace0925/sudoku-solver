import pygame, sys
from config import *
from button import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = BOARD
        self.selected = None
        self.mousePos = None
        self.font=  pygame.font.SysFont("arial", CELL_SIZE//2)
        self.state = "game"
        self.gameButton = []
        self.menuButton = []
        self.endButton = []
        self.loadBtn()

    # run the game
    def run(self):
        while self.running:
            if self.state == 'game':
                self.game_events()
                self.game_update()
                self.game_draw()
        pygame.quit()
        sys.exit()

    ####################################################################################################################
    # handle events from pygame
    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouse_clicked()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None

    def game_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.gameButton:
            button.update(self.mousePos)

    def game_draw(self):
        self.window.fill(WHITE)

        for button in self.gameButton:
            button.draw(self.window)

        if self.selected:
            self.draw_selected_cell(self.window, self.selected)

        self.draw_numbers(self.window)

        self.draw_grid(self.window)
        pygame.display.update()

    ####################################################################################################################

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
            pygame.draw.line(window, BLACK, (x * CELL_SIZE + GRID_POSITION[0], GRID_POSITION[1]),
                             (x * CELL_SIZE + GRID_POSITION[0], GRID_POSITION[1] + GRID_HEIGHT), 1 if x % 3 else 4)

            pygame.draw.line(window, BLACK, (GRID_POSITION[0], x * CELL_SIZE + GRID_POSITION[1]),
                             (GRID_POSITION[0] + GRID_WIDTH, x * CELL_SIZE + GRID_POSITION[1]), 1 if x % 3 else 4)

    def draw_selected_cell(self, window, selected_pos):
        pygame.draw.rect(window, GREEN, (selected_pos[1]*CELL_SIZE+GRID_POSITION[0], selected_pos[0]*CELL_SIZE+GRID_POSITION[1], CELL_SIZE, CELL_SIZE))

    def loadBtn(self):
        self.gameButton.append(Button(20, 40, 100, 50, "play"))

    def text_to_screen(self, text, pos, window):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)

    def draw_numbers(self, window):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col != 0:
                    pos = [j*CELL_SIZE+GRID_POSITION[0]+20, i*CELL_SIZE+GRID_POSITION[1]+10]
                    self.text_to_screen(str(col), pos, window)
