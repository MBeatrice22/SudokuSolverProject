def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()  # Împarte textul în cuvinte
            return len(words)
    except FileNotFoundError:
        print(f"Fișierul {file_path} nu a fost găsit.")
        return 0

# Calea către fișierul de pe Desktop
file_path = r'C:\Users\Motoc\Desktop\exempluL7.txt'

# Apelăm funcția și afișăm rezultatul
print(f"Numărul total de cuvinte din fișier este: {count_words_in_file(file_path)}")
