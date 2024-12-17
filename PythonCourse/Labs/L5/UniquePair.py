def unique_pair_sum(nums, target):
    seen = set()  # Set pentru a salva numerele deja întâlnite
    pairs = set()  # Set pentru a salva perechile unice

    for num in nums:
        complement = target - num  # Calculăm complementul
        if complement in seen:
            # Adăugăm perechea în set, asigurându-ne că a <= b
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)  # Adăugăm numărul curent în setul 'seen'

    return pairs

# Citirea numărului de elemente și a listei de numere de la tastatură
nums = list(map(int, input("Introduceti numerele (separate prin spatiu): ").split()))
target = int(input("Introduceti valoarea tinta: "))

# Obținem perechile unice
result = unique_pair_sum(nums, target)

print("Perechile unice care adunate dau valoarea tinta:", result)