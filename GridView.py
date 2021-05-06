import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class GridView:
    def draw(self, win, grid, rows, width):
        gap = width // rows
        win.fill(WHITE)
        for row in grid:
            for cell in row:
                draw_cell(cell, win, gap)

        draw_grid(win, rows, width, gap)
        pygame.display.update()


def draw_grid(win, rows, width, gap):
        for i in range(rows):
            pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))

        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

def draw_cell(cell, win, gap):
    color = WHITE
    
    if cell.is_start:
        color = GREEN
    elif cell.is_end:
        color = RED
    elif cell.is_path:
        color = ORANGE
    elif cell.visited:
        color = PURPLE
    elif cell.is_obstacle:
        color = BLACK
    elif cell.is_neighbour:
        color = TURQUOISE

    x = cell.col * gap
    y = cell.row * gap

    pygame.draw.rect(win, color, (x, y, gap, gap))