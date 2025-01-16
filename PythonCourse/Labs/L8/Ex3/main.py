# main.py
from geometry.circle import area as circle_area, circumference as circle_circumference
from geometry.rectangle import area as rectangle_area, perimeter as rectangle_perimeter


def main():
    # Citirea datelor de la utilizator pentru cerc
    radius = float(input("Introduceti raza cercului: "))

    # Calcularea ariei și circumferinței cercului
    print(f"Aria cercului este: {circle_area(radius)}")
    print(f"Circumferința cercului este: {circle_circumference(radius)}")

    # Citirea datelor de la utilizator pentru dreptunghi
    length = float(input("Introduceti lungimea dreptunghiului: "))
    width = float(input("Introduceti lățimea dreptunghiului: "))

    # Calcularea ariei și perimetrului dreptunghiului
    print(f"Aria dreptunghiului este: {rectangle_area(length, width)}")
    print(f"Perimetrul dreptunghiului este: {rectangle_perimeter(length, width)}")


if __name__ == "__main__":
    main()
