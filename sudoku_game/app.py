import sys
from sudoku_game.button import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = BOARD
        self.selected = None
        self.mousePos = None
        self.font = pygame.font.SysFont("arial", CELL_SIZE // 2)
        self.state = "game"
        self.finished = False
        self.cellChanged=  False
        self.gameButton = []
        self.menuButton = []
        self.endButton = []
        self.lockedCells = []
        self.incorrectCells = []
        self.load()

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
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.lockedCells:
                    if self.is_int(event.unicode):
                        self.grid[self.selected[0]][self.selected[1]] = int(event.unicode)
                        self.cellChanged = True

    def game_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.gameButton:
            button.update(self.mousePos)

        if self.cellChanged:
            self.incorrectCells = []
            if self.filled_grid():
                self.validate_all_cells()

    def game_draw(self):
        self.window.fill(WHITE)

        #for button in self.gameButton:
         #   button.draw(self.window)

        if self.selected:
            self.draw_selected_cell(self.window, self.selected)

        self.draw_locked_cell(self.window, self.lockedCells)
        self.draw_error_cell(self.window, self.incorrectCells)

        self.draw_numbers(self.window)

        self.draw_grid(self.window)
        pygame.display.update()
        self.cellChanged = False

    ####################################################################################################################

    def mouse_clicked(self):
        if self.mousePos[0] < GRID_POSITION[0] or self.mousePos[0] > GRID_POSITION[0] + GRID_WIDTH:
            return False
        if self.mousePos[1] < GRID_POSITION[1] or self.mousePos[1] > GRID_POSITION[1] + GRID_HEIGHT:
            return False
        return (self.mousePos[1] - GRID_POSITION[1]) // CELL_SIZE, (self.mousePos[0] - GRID_POSITION[0]) // CELL_SIZE

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
        pygame.draw.rect(window, GREEN, (
            selected_pos[1] * CELL_SIZE + GRID_POSITION[0], selected_pos[0] * CELL_SIZE + GRID_POSITION[1], CELL_SIZE,
            CELL_SIZE))

    def text_to_screen(self, text, pos, window):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)

    def draw_numbers(self, window):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col != 0:
                    pos = [j * CELL_SIZE + GRID_POSITION[0] + 20, i * CELL_SIZE + GRID_POSITION[1] + 10]
                    self.text_to_screen(str(col), pos, window)

    def load(self):
        self.gameButton.append(Button(20, 40, 100, 50, "play"))
        # locking cells that are given
        for i, row in enumerate(self.grid):
            for j, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([i, j])

    def draw_locked_cell(self, window, lockedCells):
        for cell in lockedCells:
            pygame.draw.rect(window, DARK_GRAY, (
                cell[1] * CELL_SIZE + GRID_POSITION[0], cell[0] * CELL_SIZE + GRID_POSITION[1], CELL_SIZE, CELL_SIZE))

    def draw_error_cell(self, window, error_cells):
        for cell in error_cells:
            pygame.draw.rect(window, RED, (
                cell[1] * CELL_SIZE + GRID_POSITION[0], cell[0] * CELL_SIZE + GRID_POSITION[1], CELL_SIZE, CELL_SIZE))

    def is_int(self, n):
        try:
            int(n)
            return True
        except:
            return False

########################################################################################################################
    def filled_grid(self):
        for row in self.grid:
            for col in row:
                if col == 0:
                    return False
        return True

    def validate_all_cells(self):
        self.check_rows()
        self.check_cols()
        self.check_square()

    def check_rows(self):
        for y, col in enumerate(self.grid):
            options = [1,2,3,4,5,6,7,8,9]
            for i in range(9):
                if self.grid[y][i] in options and [y,i] in self.lockedCells:
                    options.remove(self.grid[y][i])
                    print(options)
                else:
                    if [y,i] not in self.lockedCells and [y,i] not in self.incorrectCells:
                        self.incorrectCells.append([y,i])
                        print("error in row")

    def check_cols(self):
        for y in range(9):
            options = [1,2,3,4,5,6,7,8,9]
            for i, row in enumerate(self.grid):
                if self.grid[y][i] in options and [y,i] in self.lockedCells:
                    options.remove(self.grid[y][i])
                else:
                    if [y, i] not in self.lockedCells and [y, i] not in self.incorrectCells:
                        self.incorrectCells.append([y,i])
                        print("error in col")

    def check_square(self):
        for x in range(3):
            for y in range(3):
                options = [1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    for j in range(3):
                        if self.grid[x*3+i][y*3+j] in options and [x*3+i, y*3+j] in self.lockedCells:
                            options.remove(self.grid[x*3+i][y*3+j])
                        else:
                            if [x*3+i, y*3+j] not in self.lockedCells and [x*3+i, y*3+j] not in self.incorrectCells:
                                self.incorrectCells.append([x*3+i, y*3+j])
                                print("error in square")
