# Funcție pentru a elimina vocalele dintr-un șir
def remove_vowels(input_string):
    vowels = "aeiouyĂăÎîÂâAEIOUY"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result
# Program principal
input_string = input("Introduceti un șir de caractere: ")
# Eliminarea vocalelor din string
output_string = remove_vowels(input_string)
# Afișarea rezultatului
print(f"Șirul după eliminarea vocalelor: {output_string}")
