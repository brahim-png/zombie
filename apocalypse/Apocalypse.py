# apocalypse/apocalypse.py
from entities.zombie import Zombie
from entities.human import Human
from grid.grid import Grid

class Apocalypse(Grid):
    def __init__(self, grid_height, grid_width, zombie_list=None, human_list=None):
        super().__init__(grid_height, grid_width)
        self.zombies = zombie_list or []
        self.humans = human_list or []

    def add_zombie(self, row, col):
        """Add a zombie to the simulation at a specific position."""
        self.zombies.append(Zombie(row, col))

    def add_human(self, row, col):
        """Add a human to the simulation at a specific position."""
        self.humans.append(Human(row, col))

    def move_zombies(self):
        """Move all zombies in the simulation (dummy implementation)."""
        for zombie in self.zombies:
            new_row = zombie.row + 1  # Move zombie down for simplicity
            if new_row < self.get_height():  # Prevent moving out of bounds
                zombie.move(new_row, zombie.col)

    def move_humans(self):
        """Move all humans in the simulation (dummy implementation)."""
        for human in self.humans:
            new_col = human.col + 1  # Move human right for simplicity
            if new_col < self.get_width():  # Prevent moving out of bounds
                human.move(human.row, new_col)
