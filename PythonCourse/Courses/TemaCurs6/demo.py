# demo.py

from data_processor import read_csv, filter_data, write_csv

# Citește datele din fișierul CSV
data = read_csv('people.csv')

# Filtrează datele pentru orașul New York
filtered_data = filter_data(data, 'City', 'New York')

# Scrie datele filtrate într-un nou fișier CSV
write_csv(filtered_data, 'filtered_people.csv')

print("Fișierul CSV cu datele filtrate a fost creat.")
