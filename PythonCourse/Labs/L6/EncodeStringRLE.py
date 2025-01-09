def rle_encode(word):
    encoded_word = ""
    i = 0
    while i < len(word):
        count = 1
        while i + 1 < len(word) and word[i] == word[i + 1]:
            count += 1
            i += 1
        encoded_word += str(count) + word[i]
        i += 1
    return encoded_word

# Citim propoziția de la tastatură
word = input("Introduceti un cuvant: ")

# Aplicăm RLE
encoded_word = rle_encode(word)

# Afișăm rezultatul codificat
print("Cuvantul codificat RLE este:", encoded_word)
