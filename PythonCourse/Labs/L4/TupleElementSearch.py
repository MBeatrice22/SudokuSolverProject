# Funcția pentru a căuta un element într-un tuplu
def search_element_in_tuple(tup, element):
    if element in tup:
        return f"Elementul {element} se află în tuplu."
    else:
        return f"Elementul {element} nu se află în tuplu."

# Citirea unui șir de caractere de la tastatură pentru tuplu
input_string = input("Introduceti elementele tuplului (separate prin virgula): ")

# Conversia șirului într-un tuplu de numere întregi
input_tuple = tuple(int(x) for x in input_string.split(","))

# Afișarea tuplului
print(f"Tuplul este: {input_tuple}")

# Citirea elementului pe care dorești să-l cauți
search_value = int(input("Introduceti elementul pe care doriti sa-l cautati in tuplu: "))

# Căutăm elementul în tuplu
result = search_element_in_tuple(input_tuple, search_value)
print(result)
