import math

# Funcția pentru calcularea distanței între două puncte în 2D
def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Citirea coordonatelor de la tastatură
x1 = int(input("Introduceți coordonata x1 a primului punct: "))
y1 = int(input("Introduceți coordonata y1 a primului punct: "))
x2 = int(input("Introduceți coordonata x2 a celui de-al doilea punct: "))
y2 = int(input("Introduceți coordonata y2 a celui de-al doilea punct: "))

# Calcularea distanței
dist = distance_2d(x1, y1, x2, y2)

# Afișarea rezultatului
print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este: {dist}")