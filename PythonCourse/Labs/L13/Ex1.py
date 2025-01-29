import os

def rename_files_in_directory(directory):
    try:
        # Obține lista fișierelor din director
        files = os.listdir(directory)

        # Parcurge fiecare fișier din director
        for file_name in files:
            # Căutăm doar fișiere, nu și directoare
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                # Construim noul nume pentru fișier
                new_name = "renamed_" + file_name
                new_file_path = os.path.join(directory, new_name)

                # Redenumim fișierul
                os.rename(file_path, new_file_path)
                print(f"Fișierul '{file_name}' a fost redenumit în '{new_name}'.")

    except Exception as e:
        print(f"A apărut o eroare: {e}")

# Exemplu de utilizare:
folder_path = input("Introduceți calea directorului: ").strip()  # Folosim strip pentru a elimina eventualele spații sau ghilimele
rename_files_in_directory(folder_path)

