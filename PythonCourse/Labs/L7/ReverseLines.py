def reverse_lines(input_file, output_file):
    try:
        # Deschidem fișierul original pentru citire
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Deschidem fișierul de ieșire pentru scriere
            with open(output_file, 'w', encoding='utf-8') as outfile:
                # Citim fiecare rând din fișier
                for line in infile:
                    # Inversăm caracterele din fiecare rând
                    reversed_line = line.strip()[::-1]  # strip elimină eventualele spații la capete
                    # Scriem rândul inversat în fișierul de ieșire
                    outfile.write(reversed_line + '\n')
        print(f"Fișierul '{output_file}' a fost creat cu succes!")
    except FileNotFoundError:
        print(f"Fișierul {input_file} nu a fost găsit.")
    except IOError:
        print(f"A apărut o eroare la citirea sau scrierea fișierelor.")

# Exemplu de utilizare:
input_file = r'C:\Users\Motoc\Desktop\exempluL7.txt'
output_file = r'C:\Users\Motoc\Desktop\output_exempluL7.txt'

reverse_lines(input_file, output_file)
