def filter_lines(input_file, output_file, keyword):
    try:
        # Deschidem fișierul original pentru citire
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Deschidem fișierul de ieșire pentru scriere
            with open(output_file, 'w', encoding='utf-8') as outfile:
                # Citim fiecare rând din fișier
                for line in infile:
                    # Dacă cuvântul cheie se află în rând, scriem rândul în fișierul de ieșire
                    if keyword.lower() in line.lower():  # Comparăm fără a ține cont de majuscule/minuscule
                        outfile.write(line)
        print(f"Fișierul '{output_file}' a fost creat cu succes!")
    except FileNotFoundError:
        print(f"Fișierul {input_file} nu a fost găsit.")
    except IOError:
        print(f"A apărut o eroare la citirea sau scrierea fișierelor.")

# Citirea cuvântului cheie de la tastatură
keyword = input("Introduceți cuvântul cheie: ")

# Exemplu de utilizare:
input_file = r'C:\Users\Motoc\Desktop\input.txt'
output_file = r'C:\Users\Motoc\Desktop\output_filtered.txt'

filter_lines(input_file, output_file, keyword)
