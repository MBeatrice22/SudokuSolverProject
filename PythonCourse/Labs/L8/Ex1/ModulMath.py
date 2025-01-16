import math

# Citirea datelor de la tastatură
num = int(input("Introduceti un numar pentru a calcula radacina patrata si factorialul: "))
angle = float(input("Introduceti unghiul in grade pentru a calcula sinusul: "))

# 1. Calcularea rădăcinii pătrată a unui număr
sqrt_num = math.sqrt(num)

# 2. Calcularea factorialului unui număr
factorial_num = math.factorial(num)

# 3. Calcularea valorii sinusului unui unghi dat în grade
# Trebuie să convertim unghiul din grade în radiani, pentru că funcția sin() din math lucrează cu radiani
angle_radians = math.radians(angle)
sin_value = math.sin(angle_radians)

# Output
print(f"Rădăcina pătrată a {num} este {sqrt_num}")
print(f"Factorialul lui {num} este {factorial_num}")
print(f"Sinusul unghiului de {angle} grade este {sin_value}")
