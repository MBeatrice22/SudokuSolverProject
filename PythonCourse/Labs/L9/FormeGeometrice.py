import math


class Shape:
    def area(self):
        """Metodă de bază, care va fi suprascrisă de clasele derivate."""
        pass

    def __str__(self):
        """Metodă pentru reprezentarea textuală a formei geometrice."""
        return "Shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculează aria cercului (π * r^2)."""
        return math.pi * self.radius ** 2

    def __str__(self):
        """Reprezentare textuală a cercului."""
        return f"Circle with radius {self.radius} has area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculează aria dreptunghiului (lățime * înălțime)."""
        return self.width * self.height

    def __str__(self):
        """Reprezentare textuală a dreptunghiului."""
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"


# Exemplu de utilizare:
circle = Circle(5)
rectangle = Rectangle(10, 4)

print(circle)  # "Circle with radius 5 has area 78.54"
print(rectangle)  # "Rectangle with width 10 and height 4 has area 40"
