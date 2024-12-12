def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Se citesc date de la tastatura
number = int(input("Introduceti un numar: "))

# Se calculeaza si se printeaza factorialul
print(f"Factorialul numarului {number} este {factorial(number)}")