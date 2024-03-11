import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from fifteen import Fifteen  # Make sure your fifteen.py is in the same directory

class FifteenGUI:
    def __init__(self, root):
        self.game = Fifteen()
        self.root = root
        self.root.title("15 Puzzle Game")
        self.tiles = []
        self.create_widgets()

    def create_widgets(self):
        """Creates and grids all the widgets."""
        self.font = tkFont.Font(family='Helvetica', size=12, weight='bold')
        for i in range(16):
            button = tk.Button(self.root, text='', font=self.font, height=2, width=4,
                               command=lambda index=i: self.make_move(index))
            button.grid(row=i // 4, column=i % 4, sticky='nsew')
            self.tiles.append(button)
        self.update_tiles()

        shuffle_button = tk.Button(self.root, text='Shuffle', font=self.font, command= self.shuffle())
        shuffle_button.grid(row=4, column=0, columnspan=4, sticky='nsew')

    def shuffle(self):
        """Shuffles the tiles and updates the GUI."""
        self.game.shuffle()
        self.update_tiles()

    def make_move(self, index):
        """Attempts to make a move and updates the GUI."""
        val = self.game.tiles.flat[index]
        if val != 0:
            self.game.update(val)
            self.update_tiles()
            if self.game.is_solved():
                messagebox.showinfo("Puzzle Solved", "Congratulations! You've solved the puzzle!")

    def update_tiles(self):
        """Updates the tiles on the GUI to match the game state."""
        for i, tile in enumerate(self.tiles):
            val = self.game.tiles.flat[i]
            tile.config(text=str(val) if val != 0 else '')
            tile.config(bg='coral' if val != 0 else 'light grey')

if __name__ == '__main__':
    root = tk.Tk()
    app = FifteenGUI(root)
    root.mainloop()

