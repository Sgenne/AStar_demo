
class Cell:
        def __init__(self, row, col):
            self.row = row
            self.col = col 
            self.is_obstacle = False
            self.is_start = False
            self.is_end = False
            self.is_path = False
            self.is_neighbour = False
            self.predecessor = None
            self.total_cost = float("inf")
            self.estimated_cost = 0
            self.visited = False

        def reset(self):
            self.is_obstacle = False
            self.is_start = False
            self.is_end = False
            self.is_neighbour = False
            self.visited = False
            self.predecessor = None
            self.total_cost = float("inf")
            self.estimated_cost = 0
            self.is_path = False
        
        def sum(self):
            return self.total_cost + self.estimated_cost
        
        def __lt__(self, other):
            return False
        
        def __str__(self) -> str:
            return f"{self.row}, {self.col}"