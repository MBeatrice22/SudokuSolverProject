# data_processor.py

import csv

def read_csv(filename):
    """
    Citește un fișier CSV și returnează conținutul său ca o listă de dicționare.
    Fiecare dicționar reprezintă un rând din fișier, cu cheile fiind numele coloanelor.
    """
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def filter_data(data, key, value):
    """
    Filtrează o listă de dicționare pe baza unei perechi cheie-valoare.
    """
    return [row for row in data if row[key] == value]

def write_csv(data, filename):
    """
    Scrie datele într-un fișier CSV.
    """
    if data:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = data[0].keys()  # Extragem numele coloanelor din primul dicționar
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
