# Citim propoziția de la tastatură
sentence = input("Introdu un cuvant: ")

# Inversăm propoziția (ordinea cuvintelor)
reversed_sentence = ' '.join(sentence.split()[::-1])

# Afișăm propoziția inversată
print("Propoziția inversată este:", reversed_sentence)
