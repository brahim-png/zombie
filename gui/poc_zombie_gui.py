# gui/poc_zombie_gui.py
import pygame
import sys
from gui.interactions import Interactions
from Simulation.apocalypse import Apocalypse
from entities.zombie import Zombie
from entities.human import Human

CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

def run_gui():
    pygame.init()

    # Create Apocalypse instance
    apocalypse = apocalypse(30, 40)  # Example grid size 30x40

    # Add some zombies and humans
    zombie1 = Zombie(5, 5)
    zombie2 = Zombie(10, 10)
    human1 = Human(15, 15)
    human2 = Human(20, 20)

    apocalypse.add_zombie(zombie1)
    apocalypse.add_zombie(zombie2)
    apocalypse.add_human(human1)
    apocalypse.add_human(human2)

    interactions = Interactions(apocalypse.zombies, apocalypse.humans, apocalypse)

    # Create screen
    grid_height = apocalypse.get_height()
    grid_width = apocalypse.get_width()
    screen = pygame.display.set_mode((grid_width * CELL_SIZE, grid_height * CELL_SIZE))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        interactions.zombie_chase()  # Update zombie movement
        interactions.check_for_attack()  # Check for attacks

        screen.fill(WHITE)

        # Draw the grid
        for row in range(grid_height):
            for col in range(grid_width):
                color = WHITE
                if not apocalypse.is_empty(row, col):
                    color = GRAY
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw zombies (red)
        for zombie in apocalypse.zombies:
            row, col = zombie.get_position()
            pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        # Draw humans (green)
        for human in apocalypse.humans:
            row, col = human.get_position()
            pygame.draw.circle(screen, GREEN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        pygame.display.flip()
        clock.tick(10)  # Limit to 10 FPS
