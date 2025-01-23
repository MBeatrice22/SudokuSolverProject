def citeste_si_suma_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, 'r') as fisier:
            for linie in fisier:
                try:
                    suma += float(linie.strip())  # Convertim linia la numar
                except ValueError:
                    print(f"Atenție: Linia '{linie.strip()}' nu conține un număr valid.")
        return suma
    except FileNotFoundError:
        return f"Eroare: Fișierul '{nume_fisier}' nu a fost găsit."
    except IOError:
        return "Eroare: Nu am putut citi fișierul."

# Exemplu de utilizare
nume_fisier = "C:\\Users\\Motoc\\Desktop\\numere.txt"
  # Înlocuiește cu calea fișierului tău
rezultatul = citeste_si_suma_fisier(nume_fisier)
print(f"Suma numerelor din fișier este: {rezultatul}")
