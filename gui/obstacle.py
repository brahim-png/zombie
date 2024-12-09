# grid/obstacle.py
class Obstacle:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        """Return the position of the obstacle."""
        return (self.row, self.col)

    def set_position(self, row, col):
        """Update the position of the obstacle."""
        self.row = row
        self.col = col
