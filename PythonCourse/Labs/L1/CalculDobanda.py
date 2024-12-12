credit = float(input("Introduceti suma creditului: "))  # Suma creditului
rate = float(input("Introduceti rata dobanzii (in procente): "))  # Rata
timp = float(input("Introduceti timpul in ani: "))  # Timpul în ani
dobanda = (credit * rate * timp) / 100
print(f"Dobanda este: {dobanda}")