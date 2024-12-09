# entities/zombie.py
class Zombie:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.health = 100  # Zombies have health, they can be "killed"

    def get_position(self):
        """Return the current position of the zombie."""
        return (self.row, self.col)

    def move(self, row, col):
        """Move the zombie to a new position."""
        self.row = row
        self.col = col

    def is_alive(self):
        """Check if the zombie is still alive."""
        return self.health > 0

    def attack(self, human):
        """Attack a human if in range (simple for now)."""
        if abs(self.row - human.row) <= 1 and abs(self.col - human.col) <= 1:
            human.take_damage(10)

    def take_damage(self, damage):
        """Zombies take damage."""
        self.health -= damage
