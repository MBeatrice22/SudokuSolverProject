import tkinter as tk
from tkinter import messagebox


# Algoritmul de backtracking pentru rezolvarea Sudoku-ului
def is_valid(board, row, col, num):
    # Verifica linia
    for i in range(9):
        if board[row][i] == num:
            return False

    # Verifica coloana
    for i in range(9):
        if board[i][col] == num:
            return False

    # Verifica sub-grila 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# Crearea interfeței grafice
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.buttons = [[None for _ in range(9)] for _ in range(9)]

        self.create_grid()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                self.buttons[row][col] = tk.Entry(self.root, width=5, font=('Arial', 18), borderwidth=2, relief="solid",
                                                  justify='center')
                self.buttons[row][col].grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col].bind("<Button-1>", lambda event, r=row, c=col: self.on_click(r, c))

    def on_click(self, row, col):
        def set_number(event):
            try:
                num = int(event.widget.get())
                if 1 <= num <= 9 and is_valid(self.board, row, col, num):
                    self.board[row][col] = num
                    self.buttons[row][col].delete(0, tk.END)
                    self.buttons[row][col].insert(0, str(num))
                else:
                    messagebox.showerror("Invalid", "Numărul nu este valid!")
            except ValueError:
                pass

        self.buttons[row][col].bind("<Return>", set_number)

    def solve_sudoku(self):
        # Convertește valoarea din interfață în matrice
        for row in range(9):
            for col in range(9):
                val = self.buttons[row][col].get()
                if val != "":
                    self.board[row][col] = int(val)

        if solve(self.board):
            for row in range(9):
                for col in range(9):
                    self.buttons[row][col].delete(0, tk.END)
                    if self.board[row][col] != 0:
                        self.buttons[row][col].insert(0, str(self.board[row][col]))
        else:
            messagebox.showinfo("Eroare", "Nu se poate rezolva acest Sudoku!")

    def reset(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = 0
                self.buttons[row][col].delete(0, tk.END)


# Crează fereastra principală
root = tk.Tk()
sudoku_gui = SudokuGUI(root)

# Butoane pentru a rezolva și a reseta Sudoku-ul
solve_button = tk.Button(root, text="Rezolvă Sudoku", font=('Arial', 18), command=sudoku_gui.solve_sudoku)
solve_button.grid(row=9, column=0, columnspan=3, pady=10)

reset_button = tk.Button(root, text="Resetează", font=('Arial', 18), command=sudoku_gui.reset)
reset_button.grid(row=9, column=3, columnspan=3, pady=10)

root.mainloop()
