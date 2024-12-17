from collections import Counter
import string

def word_frequency(text):
    # Transformăm textul în litere mici și îndepărtăm semnele de punctuație
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Împarțim textul în cuvinte și numărăm frecvențele folosind Counter
    words = text.split()
    return dict(Counter(words))

# Citim textul de la tastatură
text = input("Introduceti un text: ")

# Obținem frecvența cuvintelor din text
result = word_frequency(text)

# Afișăm dicționarul cu frecvențele cuvintelor
print("Frecvențele cuvintelor din text:")
for word, count in result.items():
    print(f"'{word}': {count}")
