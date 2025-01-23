def imparte_numere(numarator, numitor):
    try:
        rezultat = numarator / numitor
        return rezultat
    except ZeroDivisionError:
        return "Eroare: Împărțire la zero!"

# Citire numere de la tastatură
try:
    numarator = float(input("Introduceti numaratorul: "))
    numitor = float(input("Introduceti numitorul: "))
    print(imparte_numere(numarator, numitor))
except ValueError:
    print("Eroare: Introduceti un numar valid!")
