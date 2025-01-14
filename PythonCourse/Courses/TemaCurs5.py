import os

def citeste_filme():
    filme = {}
    cale_fisier = os.path.join(os.path.expanduser('~'), 'Desktop', 'movies.txt')

    try:
        with open(cale_fisier, 'r') as f:
            for linie in f:
                titlu, evaluare = linie.strip().split(', ')
                filme[titlu] = int(evaluare)
    except FileNotFoundError:
        print(f"Fișierul {cale_fisier} nu a fost găsit!")
    return filme

def salveaza_filme(filme):
    cale_fisier = os.path.join(os.path.expanduser('~'), 'Desktop', 'movies.txt')

    with open(cale_fisier, 'w') as f:
        for titlu, evaluare in filme.items():
            f.write(f'{titlu}, {evaluare}\n')

def afiseaza_filme(filme):
    if filme:
        for titlu, evaluare in sorted(filme.items(), key=lambda x: x[1], reverse=True):
            print(f'{titlu} - Evaluare: {evaluare}')
    else:
        print("Nu sunt filme de afișat.")

def adauga_film(filme):
    titlu = input("Introduceți titlul filmului: ")
    evaluare = int(input("Introduceți evaluarea (1-5): "))
    filme[titlu] = evaluare

def actualizeaza_evaluare(filme):
    titlu = input("Introduceți titlul filmului: ")
    if titlu in filme:
        evaluare = int(input(f"Noua evaluare pentru {titlu} (1-5): "))
        filme[titlu] = evaluare
    else:
        print("Film inexistent.")

def sterge_film(filme):
    titlu = input("Introduceți titlul filmului: ")
    if titlu in filme:
        del filme[titlu]
    else:
        print("Film inexistent.")


def main():
    filme = citeste_filme()

    while True:
        print("\nMeniu:")
        print("1. Vizualizați filmele și evaluările")
        print("2. Adăugați un film nou")
        print("3. Actualizați evaluarea unui film")
        print("4. Ștergeți un film")
        print("5. Salvați modificările și ieșiți")

        optiune = input("Alegeți o opțiune (1-5): ")

        if optiune == '1':
            afiseaza_filme(filme)
        elif optiune == '2':
            adauga_film(filme)
        elif optiune == '3':
            actualizeaza_evaluare(filme)
        elif optiune == '4':
            sterge_film(filme)
        elif optiune == '5':
            salveaza_filme(filme)
            print("Modificările au fost salvate. La revedere!")
            break
        else:
            print("Opțiune invalidă.")


if __name__ == "__main__":
    main()
