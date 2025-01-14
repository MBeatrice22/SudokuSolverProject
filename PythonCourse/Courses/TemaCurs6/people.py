import csv

# Datele pe care dorim să le salvăm în fișierul CSV
data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
]

# Crearea fișierului CSV
with open("people.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Fișierul CSV a fost creat cu succes!")
