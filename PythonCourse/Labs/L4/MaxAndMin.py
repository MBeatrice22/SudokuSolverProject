# Funcție pentru a găsi maximul și minimul
def find_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum
# Citirea unui număr de elemente
n = int(input("Introduceți numărul de elemente: "))
# Citirea numerelor de la tastatură
numbers = []
for i in range(n):
    num = float(input(f"Introduceți numărul {i+1}: "))
    numbers.append(num)
# Găsirea valorilor maxime și minime
max_val, min_val = find_max_min(numbers)
print(f"Valoarea maximă este: {max_val}")
print(f"Valoarea minimă este: {min_val}")
