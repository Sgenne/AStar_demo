from Dijkstra import Dijkstra

class AStar(Dijkstra):
    def __init__(self, grid, start, end):
        super().__init__(grid, start, end)
        estimate_costs(grid, end)

def estimate_costs(grid, end):
    for row in grid:
        for cell in row:
            cell.estimated_cost = manhattan_distance(cell, end)

def manhattan_distance(cell1, cell2):
    return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)

