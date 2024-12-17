from collections import Counter
import string


def word_frequency(text):
    # Transformă textul în litere mici și îndepărtează semnele de punctuație
    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Împarte textul în cuvinte și numără frecvențele folosind Counter
    words = text.split()
    return dict(Counter(words))


# Citirea textului de la tastatură
text = input("Introduceti un text: ")

# Obținem frecvența cuvintelor din text
result = word_frequency(text)

# Afișăm dicționarul cu frecvențele cuvintelor
print("Frecvențele cuvintelor din text:")
for word, count in result.items():
    print(f"'{word}': {count}")
