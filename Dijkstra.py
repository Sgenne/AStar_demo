from queue import PriorityQueue
from Cell import Cell

class Dijkstra:
    def __init__(self, grid, start, end):
        self.open = PriorityQueue()
        self.grid = grid 
        self.start = start
        self.end = end
        self.done = False
        self.open.put((0, start))
        self.open_hash = {start}

        self.start.total_cost = 0
    
    def step(self):
        if not self.done and not self.open.empty():
            current_cell = self.open.get()[1]
            self.open_hash.remove(current_cell)
            current_cell.visited = True

            if current_cell == self.end:
                self.done = True
                return True

            for neighbour in get_neighbours(self.grid, current_cell):
                neighbour.is_neighbour = True
                if not neighbour.visited:
                    tmp_cost = current_cell.total_cost + 1

                    if tmp_cost < neighbour.total_cost:
                        neighbour.total_cost = tmp_cost
                        neighbour.predecessor = current_cell
                    
                    if neighbour not in self.open_hash:
                        self.open_hash.add(neighbour)
                        self.open.put((neighbour.sum(), neighbour))

def get_neighbours(grid, cell):
        neighbours = []

        if cell.row < len(grid) - 1 and not grid[cell.row + 1][cell.col].is_obstacle:
            neighbours.append(grid[cell.row + 1][cell.col])
      
        if cell.row > 0 and not grid[cell.row - 1][cell.col].is_obstacle:
            neighbours.append(grid[cell.row - 1][cell.col])
        
        if cell.col < len(grid) - 1 and not grid[cell.row][cell.col + 1].is_obstacle:
            neighbours.append(grid[cell.row][cell.col + 1])
        
        if cell.col > 0 and not grid[cell.row][cell.col - 1].is_obstacle:
            neighbours.append(grid[cell.row][cell.col - 1])
    
        return neighbours


