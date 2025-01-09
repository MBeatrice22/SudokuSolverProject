import tkinter as tk
from tkinter import messagebox


# Funcție pentru a verifica dacă este posibil să pui un număr într-o celulă
def este_valid(sudoku, row, col, num):
    # Verifică pe rând
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Verifică pe coloană
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Verifică în sub-grila 3x3
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True


# Funcție pentru a rezolva Sudoku-ul folosind backtracking
def rezolva_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if este_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if rezolva_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True


# Funcție pentru a actualiza Sudoku-ul cu valorile introduse de utilizator
def actualizeaza_sudoku():
    global sudoku
    try:
        for row in range(9):
            for col in range(9):
                val = input_fields[row][col].get()
                if val:
                    sudoku[row][col] = int(val)
                else:
                    sudoku[row][col] = 0
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți doar cifre între 1 și 9.")
        return

    # Rezolvă Sudoku-ul
    if rezolva_sudoku(sudoku):
        actualizeaza_campuri()
    else:
        messagebox.showerror("Eroare", "Sudoku-ul nu are soluție!")


# Funcție pentru a actualiza câmpurile din GUI cu soluția Sudoku-ului
def actualizeaza_campuri():
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] != 0:
                input_fields[row][col].delete(0, tk.END)
                input_fields[row][col].insert(0, str(sudoku[row][col]))
            else:
                input_fields[row][col].delete(0, tk.END)


# Crearea ferestrei principale
root = tk.Tk()
root.title("Sudoku")

# Sudoku-ul inițial (poți schimba acest puzzle cu altul)
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Crearea câmpurilor de input pentru Sudoku
input_fields = [[None for _ in range(9)] for _ in range(9)]

# Definirea culorilor pentru sub-grilele 3x3
sub_grid_colors = [
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow',
     'lightyellow'],
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow',
     'lightyellow'],
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow',
     'lightyellow'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan',
     'lightcyan'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan',
     'lightcyan'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan',
     'lightcyan'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen',
     'lightgreen'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen',
     'lightgreen'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen',
     'lightgreen']
]

# Crearea câmpurilor de input și setarea bordurilor și culorilor pentru sub-grilele de 3x3
for row in range(9):
    for col in range(9):
        input_fields[row][col] = tk.Entry(root, width=5, font=("Arial", 18), justify="center", bd=2, relief="solid")
        input_fields[row][col].grid(row=row, column=col, padx=5, pady=5)

        # Setăm culoarea de fundal pentru fiecare sub-grilă 3x3
        input_fields[row][col].config(bg=sub_grid_colors[row][col])

# Adăugarea bordurilor între sub-grile
for i in range(1, 9):
    if i % 3 == 0:
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

# Buton pentru a rezolva Sudoku-ul
rezolva_button = tk.Button(root, text="Rezolvă Sudoku", font=("Arial", 14), command=actualizeaza_sudoku)
rezolva_button.grid(row=9, column=0, columnspan=9)

# Rulare interfață grafică
root.mainloop()


