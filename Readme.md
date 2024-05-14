## 8-Puzzle Solver GUI

This Python program provides a graphical user interface (GUI) for solving the classic
8-Puzzle problem.

The 8-Puzzle is a sliding puzzle with eight numbered tiles and one empty space, where the goal is to arrange the tiles in ascending order starting from the top-left corner, with the empty space at the bottom-right corner.

## Features

Interactive GUI: User-friendly interface implemented using the Tkinter library.

Random Shuffling: Ability to shuffle the puzzle tiles randomly to start a new game.

Move Counter: Keeps track of the number of moves made by the player.

Goal State Display: Displays the goal state configuration for reference during gameplay.

Win Detection: Automatically detects when the puzzle is solved and displays a congratulatory message.

## How to Use

Run the program by executing the puzzle_gui.py file.

The GUI window will open, displaying the shuffled puzzle tiles.

Click on a numbered tile adjacent to the empty space to move it into the empty space.

Continue moving tiles until the puzzle is solved.

Once solved, a message will appear congratulating the player and displaying the number
of moves made.

## Requirements

Python 3.x

Tkinter library (usually included in standard Python installations)

## Additional Information

The program utilizes the Tkinter library for creating the graphical user interface.
Puzzle tiles are represented by Tkinter buttons with text labels for the tile numbers.

The program implements a move counter to track the number of moves made by the player.

Goal state configuration is displayed for reference, helping players visualize the desired arrangement of tiles.

## Feel free to explore and enjoy solving the 8-Puzzle with this interactive GUI program!
