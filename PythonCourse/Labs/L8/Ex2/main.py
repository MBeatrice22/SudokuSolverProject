# main.py

import mathOperations


def main():
    # Citirea valorilor de la tastatură
    a = float(input("Introduceti primul numar: "))
    b = float(input("Introduceti al doilea numar: "))

    # Adunare
    suma = mathOperations.adunare(a, b)
    print(f"Suma celor doua numere este: {suma}")

    # Scadere
    diferenta = mathOperations.scadere(a, b)
    print(f"Diferența dintre cele două numere este: {diferenta}")

    # Inmultire
    produs = mathOperations.inmultire(a, b)
    print(f"Produsul celor două numere este: {produs}")

    # Impartire
    if b != 0:
        catul = mathOperations.impartire(a, b)
        print(f"Catul dintre cele două numere este: {catul}")
    else:
        print(mathOperations.impartire(a, b))  # Va apela eroarea definită în math_operations


if __name__ == "__main__":
    main()
