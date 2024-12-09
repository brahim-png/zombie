# grid/grid.py
class Grid:
    def __init__(self, grid_height, grid_width):
        # Initialize the grid dimensions and empty grid
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [[None] * grid_width for _ in range(grid_height)]  # None for empty cells
        self._obstacles = []  # List to store positions of obstacles

    def add_obstacle(self, row, col):
        """Add an obstacle to the grid."""
        if 0 <= row < self._grid_height and 0 <= col < self._grid_width:
            self._grid[row][col] = 'FULL'
            self._obstacles.append((row, col))

    def is_empty(self, row, col):
        """Check if a cell is empty."""
        return self._grid[row][col] is None

    def get_cell(self, row, col):
        """Return the current status of a cell (empty or obstacle)."""
        return self._grid[row][col]

    def get_height(self):
        """Return the height of the grid."""
        return self._grid_height

    def get_width(self):
        """Return the width of the grid."""
        return self._grid_width
