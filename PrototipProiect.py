import tkinter as tk
from tkinter import messagebox
# Funcție pentru a verifica dacă este posibil să pui un număr într-o celulă
def este_valid(sudoku, row, col, num):
    # Verificare pe linie
    if num in sudoku[row]:
        return False
    # Verificare pe coloană
    if num in [sudoku[i][col] for i in range(9)]:
        return False
    # Verificare în sub-căsuța 3x3
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
                    num = int(val)
                    if num < 1 or num > 9:
                        raise ValueError("Numărul trebuie să fie între 1 și 9.")
                    if not este_valid(sudoku, row, col, num):
                        raise ValueError("Numărul introdus nu este valid pe linie, coloană sau sub-căsuță.")
                    sudoku[row][col] = num
                else:
                    sudoku[row][col] = 0
    except ValueError as ve:
        messagebox.showerror("Eroare", str(ve))
        return
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
                # Dacă valoarea a fost introdusă de utilizator, textul va fi negru
                if initial_values[row][col]:
                    input_fields[row][col].config(fg="black")
                else:
                    input_fields[row][col].config(fg="green")
            else:
                input_fields[row][col].delete(0, tk.END)
# Crearea ferestrei principale
root = tk.Tk()
root.title("Sudoku")
# Sudoku-ul inițial necompletat
sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# Crearea câmpurilor de input pentru Sudoku
input_fields = [[None for _ in range(9)] for _ in range(9)]
# Matrice pentru a păstra valorile inițiale introduse de utilizator
initial_values = [[False for _ in range(9)] for _ in range(9)]
# Crearea Canvas-ului pentru desenarea grilei
canvas = tk.Canvas(root, width=540, height=540)
canvas.grid(row=0, column=0, padx=10, pady=10)
# Dimensiunea fiecărei celule
cell_size = 60
# Desenarea grilei Sudoku
for i in range(10):
    thickness = 3 if i % 3 == 0 else 1
    canvas.create_line(i * cell_size, 0, i * cell_size, 540, width=thickness)
    canvas.create_line(0, i * cell_size, 540, i * cell_size, width=thickness)
# Crearea câmpurilor de input pentru Sudoku
for row in range(9):
    for col in range(9):
        input_fields[row][col] = tk.Entry(root, width=2, font=("Arial", 18), justify="center", bd=0)  # Fără borduri
        input_fields[row][col].place(x=col * cell_size + 20, y=row * cell_size + 20)
        # Event handler pentru a marca valorile introduse de utilizator
        def on_keyrelease(event, r=row, c=col):
            initial_values[r][c] = True
            input_fields[r][c].config(fg="black")  # Schimbăm culoarea textului în negru pentru valorile introduse
        input_fields[row][col].bind("<KeyRelease>", on_keyrelease)
# Buton pentru a rezolva Sudoku-ul
rezolva_button = tk.Button(root, text="Rezolvă Sudoku", font=("Arial", 14), command=actualizeaza_sudoku)
rezolva_button.grid(row=9, column=0, columnspan=9, pady=10)
# Rulare interfață grafică
root.mainloop()