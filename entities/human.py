# entities/human.py
class Human:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.health = 100  # Humans have health

    def get_position(self):
        """Return the current position of the human."""
        return (self.row, self.col)

    def move(self, row, col):
        """Move the human to a new position."""
        self.row = row
        self.col = col

    def is_alive(self):
        """Check if the human is still alive."""
        return self.health > 0

    def take_damage(self, damage):
        """Humans take damage."""
        self.health -= damage

    def heal(self, health_points):
        """Humans can heal if they have the resources."""
        self.health += health_points
