from AStar import AStar
from Dijkstra import Dijkstra
import pygame 
import math
import random

from Cell import Cell
from GridView import GridView

WIDTH = 600
ROWS = 50

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A*")

def make_grid(rows, width):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j)
            grid[i].append(cell)

    return grid

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col

def empty_grid(grid):
    for row in grid:
        for cell in row:
            if not cell.is_obstacle:
                cell.reset()

def randomize(grid):
    random_factor = 0.15

    for row in grid:
        for cell in row:
            if random.uniform(0, 1) < random_factor:
                cell.is_obstacle = True



def main(win, rows, width):
    grid = make_grid(rows, width)
    view = GridView()
    pathfinder = None
    start = None
    end = None

    run = True
    while run:
        
        view.draw(win, grid, rows, width)

        if pathfinder:
            if not pathfinder.done:
                pathfinder.step()
            
            else:
                predecessor = pathfinder.end.predecessor
                while predecessor.is_path:
                    predecessor = predecessor.predecessor
                
                if predecessor.is_start:
                    pathfinder = None
                else:
                    predecessor.is_path = True
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]

                if not start:
                    start = cell
                    start.is_start = True
                
                elif not end and not cell.is_start:
                   end = cell
                   end.is_end = True
                
                elif not cell.is_end and not cell.is_start:
                    cell.is_obstacle = True
            
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                if cell == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1 and start and end and pathfinder is None:
                    pathfinder = Dijkstra(grid, start, end)
            
                if event.key == pygame.K_2 and start and end and pathfinder is None:

                    pathfinder = AStar(grid, start, end)
                
                if event.key == pygame.K_r:
                    empty_grid(grid)
                    start = None
                    end = None
                    pathfinder = None
                    randomize(grid)

                if event.key == pygame.K_e:
                    empty_grid(grid)
                    start = None
                    end = None
                    pathfinder = None

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    pathfinder = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(WIN, ROWS, WIDTH)

