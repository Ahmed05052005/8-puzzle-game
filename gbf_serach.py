import tkinter as tk
from tkinter import messagebox
import random

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver")
        self.root.geometry("300x400")
        
        self.board = tk.Frame(root)
        self.board.pack()

        self.tiles = []
        self.empty_row, self.empty_col = 2, 2  # Initial position of the empty tile
        self.goal_state = list(range(1, 9)) + [0]  # Goal state configuration
        
        self.moves = 0  # Counter to track the number of moves

        # Create move counter label
        self.move_counter_var = tk.StringVar()
        self.move_counter_label = tk.Label(root, textvariable=self.move_counter_var)
        self.move_counter_label.pack()

        self.create_board()
        self.shuffle_board()
        self.show_goal_state()

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                tile = tk.Button(self.board, text="", width=5, height=2, font=('Helvetica', 12),
                                 command=lambda i=i, j=j: self.move_tile(i, j))
                tile.grid(row=i, column=j, padx=2, pady=2)
                row.append(tile)
            self.tiles.append(row)

    def shuffle_board(self):
        numbers = list(range(1, 9))
        random.shuffle(numbers)
        numbers.append(0)  # Add 0 for the empty tile
        numbers = iter(numbers)

        for i in range(3):
            for j in range(3):
                number = next(numbers)
                self.tiles[i][j]["text"] = number
                if number == 0:
                    self.empty_row, self.empty_col = i, j

    def move_tile(self, row, col):
        if self.is_adjacent(row, col):
            self.tiles[self.empty_row][self.empty_col]["text"] = self.tiles[row][col]["text"]
            self.tiles[row][col]["text"] = ""
            self.empty_row, self.empty_col = row, col
            self.moves += 1  # Increment move counter
            self.move_counter_var.set(f"Moves: {self.moves}")  # Update move counter label
            if self.check_win():
                self.end_game()

    def is_adjacent(self, row, col):
        return (row == self.empty_row and abs(col - self.empty_col) == 1) or \
               (col == self.empty_col and abs(row - self.empty_row) == 1)

    def check_win(self):
        numbers = [self.tiles[i][j]["text"] for i in range(3) for j in range(3)]
        return numbers == self.goal_state

    def show_goal_state(self):
        goal_label = tk.Label(self.root, text="Goal State", font=('Helvetica', 12, 'bold'))
        goal_label.pack()
        goal_frame = tk.Frame(self.root)
        goal_frame.pack()
        for i in range(3):
            for j in range(3):
                tile = tk.Label(goal_frame, text=str(self.goal_state[i * 3 + j]), width=5, height=2, font=('Helvetica', 12))
                tile.grid(row=i, column=j, padx=2, pady=2)

    def end_game(self):
        messagebox.showinfo("Congratulations!", f"You solved the puzzle in {self.moves} moves!")
        self.root.destroy()

def main():
    root = tk.Tk()
    PuzzleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
