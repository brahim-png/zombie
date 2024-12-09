# main.py
from apocalypse.Apocalypse import Apocalypse
import gui.poc_zombie_gui as gui

def main():
    # Create an Apocalypse instance with a 10x10 grid
    apocalypse = Apocalypse(10, 10)

    # Add some zombies and humans
    apocalypse.add_zombie(2, 3)
    apocalypse.add_human(5, 5)

    # Run the GUI to visualize the simulation
    gui.run_gui(apocalypse)

if __name__ == '__main__':
    main()
