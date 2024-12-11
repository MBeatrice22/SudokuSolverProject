import random


def is_valid(board, row, col, num):
    # Verifică dacă numărul este valid pe linia respectivă
    for i in range(9):
        if board[row][i] == num:
            return False

    # Verifică dacă numărul este valid pe coloana respectivă
    for i in range(9):
        if board[i][col] == num:
            return False

    # Verifică dacă numărul este valid în sub-grila 3x3
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
            if board[row][col] == 0:  # Căutăm o celulă goală
                for num in range(1, 10):  # Încercăm toate numerele
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):  # Recursiv, încercăm să rezolvăm mai departe
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # Nu există o soluție validă
    return True  # Sudoku rezolvat


def print_board(board):
    for i in range(9):
        # Se adaugă linii de delimitare la fiecare 3 rânduri și coloane
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Linie verticală pentru fiecare 3 coloană
            print(str(board[i][j]) if board[i][j] != 0 else '.', end=" ")  # Afișează puncte pentru celulele goale
        print()


def generate_sudoku():
    # Creăm un tabel 9x9 cu toate valorile 0 (necompletat)
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Încercăm să completăm tabela cu numere
    for _ in range(10):  # Încercăm de 10 ori să umplem tabla
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if is_valid(board, row, col, num):
            board[row][col] = num

    return board


# Generăm un Sudoku
board = generate_sudoku()

# Afișăm tabla inițială (parțial completată)
print("Sudoku generat:")
print_board(board)

# Rezolvăm Sudoku
print("\nRezolvare Sudoku:")
solve(board)
print_board(board)
