# simulation.py
import random
import time
from apocalypse import Apocalypse


def initialize_simulation(grid_height, grid_width, num_zombies, num_humans, obstacle_percentage=0.1):
    """Initialize the grid with zombies, humans, and obstacles."""
    # Create obstacles
    obstacles = set()
    while len(obstacles) < int(grid_height * grid_width * obstacle_percentage):
        row = random.randint(0, grid_height - 1)
        col = random.randint(0, grid_width - 1)
        if (row, col) not in obstacles:
            obstacles.add((row, col))

    # Create humans and zombies in random locations
    humans = set()
    zombies = set()
    while len(humans) < num_humans:
        row = random.randint(0, grid_height - 1)
        col = random.randint(0, grid_width - 1)
        if (row, col) not in obstacles and (row, col) not in humans and (row, col) not in zombies:
            humans.add((row, col))

    while len(zombies) < num_zombies:
        row = random.randint(0, grid_height - 1)
        col = random.randint(0, grid_width - 1)
        if (row, col) not in obstacles and (row, col) not in zombies and (row, col) not in humans:
            zombies.add((row, col))

    return Apocalypse(grid_height, grid_width, list(obstacles), list(zombies), list(humans))


def print_grid(apocalypse):
    """Print the current state of the grid."""
    grid_copy = [row[:] for row in apocalypse.grid]  # Create a copy of the grid to modify
    for (row, col) in apocalypse.zombie_list:
        grid_copy[row][col] = 'Z'  # Mark zombies
    for (row, col) in apocalypse.human_list:
        grid_copy[row][col] = 'H'  # Mark humans
    for (row, col) in apocalypse.obstacle_list:
        grid_copy[row][col] = 'X'  # Mark obstacles

    for row in grid_copy:
        print(' '.join(row))
    print("\n" + "-" * 50 + "\n")


def run_simulation():
    """Run the zombie vs human simulation."""
    grid_height = 10
    grid_width = 10
    num_zombies = 5
    num_humans = 5
    obstacle_percentage = 0.2  # Percentage of obstacles in the grid

    apocalypse = initialize_simulation(grid_height, grid_width, num_zombies, num_humans, obstacle_percentage)

    # Simulate for 20 turns or until there are no humans left
    for turn in range(20):
        print(f"Turn {turn + 1}")
        print_grid(apocalypse)

        if apocalypse.num_humans() == 0:
            print("All humans have been caught! Zombies win!")
            break

        # Compute the distance field for zombies and humans
        zombie_distance_field = apocalypse.compute_distance_field('ZOMBIE')
        human_distance_field = apocalypse.compute_distance_field('HUMAN')

        # Move zombies and humans based on distance fields
        apocalypse.move_zombies(human_distance_field)
        apocalypse.move_humans(zombie_distance_field)

        time.sleep(1)  # Sleep for a moment to simulate the passing of time

    # End the simulation
    if apocalypse.num_humans() > 0:
        print("Humans have survived!")
    else:
        print("Zombies have taken over!")


if __name__ == "__main__":
    run_simulation()
