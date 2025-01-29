import csv


def process_csv(input_file, output_file):
    try:
        # Deschidem fișierul CSV de intrare pentru citire
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(
                infile)  # Citim fișierul folosind DictReader pentru a accesa fiecare coloană după nume

            # Creăm o listă pentru a stoca noile date cu valoarea totală
            rows = []
            for row in reader:
                # Verificăm și extragem valorile din fișier
                try:
                    cantitate = int(row['Cantitate'])  # Convertim cantitatea în număr întreg
                    pret_unitar = float(row['Pret unitar'])  # Convertim prețul unitar în float
                except ValueError as e:
                    print(f"A apărut o eroare de conversie a valorilor pentru rândul: {row}. Detalii: {e}")
                    continue

                # Calculăm valoarea totală pentru fiecare comandă
                valoare_totala = cantitate * pret_unitar  # Calculăm valoarea totală

                # Adăugăm valoarea totală ca o coloană nouă
                row['Valoare totala'] = round(valoare_totala, 2)  # Rotunjim la 2 zecimale
                rows.append(row)

        # Deschidem fișierul CSV de ieșire pentru scriere
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            # Definim numele coloanelor (header)
            fieldnames = ['Produs', 'Cantitate', 'Pret unitar', 'Valoare totala']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Scriem header-ul
            writer.writeheader()

            # Scriem fiecare rând cu datele procesate
            writer.writerows(rows)

        print(f"Fișierul a fost procesat cu succes și salvat în '{output_file}'.")

    except Exception as e:
        print(f"A apărut o eroare: {e}")


# Exemplu de utilizare:
input_file = input("Introduceți calea fișierului CSV de intrare: ")
output_file = input("Introduceți calea fișierului CSV de ieșire: ")

process_csv(input_file, output_file)
