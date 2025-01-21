import math


# Funcție pentru a calcula al n-lea număr Fibonacci folosind memoizarea
def fibonacci(n, memo={}):
    if n < 0:
        raise ValueError("Fibonacci nu este definit pentru numere negative.")
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]


# Funcție pentru a calcula aria unui cerc cu validare a inputului
def circle_area(radius):
    if radius < 0:
        raise ValueError("Raza nu poate fi negativă. Te rog să furnizezi o rază validă.")
    if radius == 0:
        return 0  # Tratarea specială a razei 0
    return math.pi * radius ** 2


# Funcție pentru a găsi valoarea maximă dintr-o listă folosind recursivitatea
def find_max(numbers):
    if not numbers:  # Verificăm imediat dacă lista este goală
        raise ValueError("Nu se poate găsi valoarea maximă într-o listă goală.")
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value


# Funcție pentru a calcula media geometrică a unei liste de numere
def geometric_mean(numbers):
    if not numbers:  # Verificăm dacă lista este goală
        raise ValueError("Nu se poate calcula media geometrică pentru o listă goală.")
    if any(num <= 0 for num in numbers):  # Verificăm dacă există numere <= 0
        raise ValueError("Toate numerele trebuie să fie pozitive pentru a calcula media geometrică.")
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))


# Funcție principală pentru a demonstra operațiile
def main():
    print("=== Fibonacci ===")
    try:
        n = int(input("Introdu un număr pentru Fibonacci: "))
        print(f"Numărul Fibonacci {n} este: {fibonacci(n)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Aria Cercului ===")
    try:
        radius = float(input("Introdu raza cercului: "))
        print(f"Aria unui cerc cu raza {radius} este: {circle_area(radius)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Găsirea valorii maxime ===")
    try:
        numbers = list(map(int, input("Introdu o listă de numere separate prin spațiu: ").split()))
        print(f"Valoarea maximă din lista {numbers} este: {find_max(numbers)}")
    except ValueError as e:
        print(f"Eroare: {e}")

    print("\n=== Media Geometrică ===")
    try:
        numbers = list(map(float, input(
            "Introdu o listă de numere pozitive separate prin spațiu pentru media geometrică: ").split()))
        print(f"Media geometrică a listei {numbers} este: {geometric_mean(numbers)}")
    except ValueError as e:
        print(f"Eroare: {e}")


# Apelăm funcția principală
main()
