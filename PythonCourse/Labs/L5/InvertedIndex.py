import string

def inverted_index(documents):
    index = {}  # Dicționarul ce va conține cuvintele și indiciile documentelor

    for i, doc in enumerate(documents):
        # Curățăm documentul de semnele de punctuație și îl transformăm în litere mici
        doc = doc.lower().translate(str.maketrans('', '', string.punctuation))

        # Împărțim documentul în cuvinte
        words = set(doc.split())  # Folosim set pentru a elimina duplicatele

        # Adăugăm cuvintele în index
        for word in words:
            if word not in index:
                index[word] = set()  # Dacă cuvântul nu există în index, îl adăugăm
            index[word].add(i)  # Adăugăm indexul documentului în setul cuvântului

    return index

#exemple de documente
documents = [
    "Acesta este primul document.",
    "Al doilea document conține cuvinte noi.",
    "Și acesta este un alt document cu cuvinte importante."
]
result = inverted_index(documents)
print(result)
