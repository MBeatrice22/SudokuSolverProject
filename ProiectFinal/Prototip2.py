import tkinter as tk  # bibliotecă necesară pentru a crea interfața grafică
from tkinter import messagebox  # bibliotecă necesară pentru a afișa mesaje de eroare
from PIL import Image, ImageTk  # biblioteca Pillow pentru a manipula imagini
import random

# Funcție pentru a verifica dacă este posibil să pui un număr într-o celulă
def este_valid(sudoku, row, col, num):
    # Verifică dacă numărul există deja pe rând
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Verifică dacă numărul există deja pe coloană
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Verifică dacă numărul există deja în sub-grila 3x3
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


# Funcție pentru a verifica dacă există erori în Sudoku
def verifica_eroare():
    erori = []

    # Verificăm pentru duplicate pe fiecare linie
    for row in range(9):
        linie = [sudoku[row][col] for col in range(9) if sudoku[row][col] != 0]
        if len(linie) != len(set(linie)):  # Dacă există duplicate
            erori.append(f"Există duplicate pe linia {row + 1}")

    # Verificăm pentru duplicate pe fiecare coloană
    for col in range(9):
        coloana = [sudoku[row][col] for row in range(9) if sudoku[row][col] != 0]
        if len(coloana) != len(set(coloana)):  # Dacă există duplicate
            erori.append(f"Există duplicate pe coloana {col + 1}")

    # Verificăm pentru duplicate în fiecare sub-grilă 3x3
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(sudoku[start_row + i][start_col + j])
            subgrid_fara_zero = [x for x in subgrid if x != 0]
            if len(subgrid_fara_zero) != len(set(subgrid_fara_zero)):  # Dacă există duplicate
                erori.append(f"Există duplicate în careul ({start_row // 3 + 1}, {start_col // 3 + 1})")

    return erori


# Funcție pentru a actualiza Sudoku-ul cu valorile introduse de utilizator
def actualizeaza_sudoku():
    global sudoku
    try:
        for row in range(9):
            for col in range(9):
                val = input_fields[row][col].get()

                # Validăm că valoarea introdusă este un număr între 1 și 9
                if val:
                    if not val.isdigit() or int(val) < 1 or int(val) > 9:
                        messagebox.showerror("Eroare", "Introduceți doar cifre între 1 și 9.")
                        return
                    sudoku[row][col] = int(val)
                else:
                    sudoku[row][col] = 0
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți doar cifre între 1 și 9.")
        return

    # Verifică erorile înainte de a rezolva Sudoku-ul
    erori = verifica_eroare()
    if erori:
        # Afișăm erorile într-un singur mesaj
        messagebox.showerror("Eroare", "\n".join(erori))
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


# Funcție pentru a reseta Sudoku-ul
def reseteaza_sudoku():
    global sudoku
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    for row in range(9):
        for col in range(9):
            input_fields[row][col].delete(0, tk.END)


# Funcție pentru a genera câteva numere aleatorii în Sudoku
def genereaza_numere_random():
    global sudoku
    numar_de_numere = random.randint(10, 20)

    for _ in range(numar_de_numere):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)

        if sudoku[row][col] == 0 and este_valid(sudoku, row, col, num):
            sudoku[row][col] = num

    actualizeaza_campuri()


# Crearea ferestrei principale
root = tk.Tk()
root.title("Sudoku")

# Încarcă și afișează imaginea
image_path = "sudokuLogo.png"
image = Image.open(image_path)
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)

label_image = tk.Label(root, image=photo)
label_image.grid(row=0, column=0, columnspan=9, pady=10)

# Inițializarea unui careu de sudoku cu toate valorile 0
sudoku = [[0 for _ in range(9)] for _ in range(9)]

# Crearea câmpurilor de input pentru Sudoku
input_fields = [[None for _ in range(9)] for _ in range(9)]

# Definirea culorilor pentru sub-grilele 3x3
sub_grid_colors = [
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow', 'lightyellow'],
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow', 'lightyellow'],
    ['lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen', 'lightyellow', 'lightyellow', 'lightyellow'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan', 'lightcyan'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan', 'lightcyan'],
    ['lightpink', 'lightpink', 'lightpink', 'lightgray', 'lightgray', 'lightgray', 'lightcyan', 'lightcyan', 'lightcyan'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen'],
    ['lightcoral', 'lightcoral', 'lightcoral', 'lightblue', 'lightblue', 'lightblue', 'lightgreen', 'lightgreen', 'lightgreen']
]

# Crearea câmpurilor de input și setarea bordurilor și culorilor pentru sub-grilele de 3x3
for row in range(9):
    for col in range(9):
        input_fields[row][col] = tk.Entry(root, width=5, font=("Arial", 18), justify="center", bd=2, relief="solid")
        input_fields[row][col].grid(row=row + 1, column=col, padx=5, pady=5)
        input_fields[row][col].config(bg=sub_grid_colors[row][col])

# Buton pentru a rezolva Sudoku-ul
rezolva_button = tk.Button(root, text="Rezolvă Sudoku", font=("Arial", 14), command=actualizeaza_sudoku)
rezolva_button.grid(row=10, column=0, columnspan=9)

# Buton pentru a reseta Sudoku-ul
reset_button = tk.Button(root, text="Resetează Sudoku", font=("Arial", 14), command=reseteaza_sudoku)
reset_button.grid(row=11, column=0, columnspan=9)

# Buton pentru a genera numere aleatorii
genereaza_random_button = tk.Button(root, text="Generează numere aleatorii", font=("Arial", 14), command=genereaza_numere_random)
genereaza_random_button.grid(row=12, column=0, columnspan=9)

# Rulare interfață grafică
root.mainloop()
