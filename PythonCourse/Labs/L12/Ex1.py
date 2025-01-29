import requests
from tabulate import tabulate


# Funcția pentru a obține și prelucra datele
def get_users_data(city_filter=None):
    try:
        # Trimite cererea GET către API
        response = requests.get('https://jsonplaceholder.typicode.com/users')

        # Verificăm dacă cererea a fost succes
        response.raise_for_status()

        # Obținem datele în format JSON
        users = response.json()

        # Filtrarea utilizatorilor pe baza orașului (dacă este specificat)
        if city_filter:
            users = [user for user in users if user['address']['city'] == city_filter]

        # Extragem și afișăm datele într-un format tabelar
        table = []
        for user in users:
            table.append([
                user['id'],
                user['name'],
                user['username'],
                user['email'],
                user['address']['city'],
                user['company']['name'],
                user['phone'],
                user['website']
            ])

        # Afișează tabelul folosind tabulate
        headers = ['ID', 'Nume', 'Username', 'Email', 'Oraș', 'Companie', 'Telefon', 'Website']
        print(tabulate(table, headers=headers, tablefmt='pretty'))

    except requests.exceptions.RequestException as e:
        # În cazul în care cererea API nu este reușită, afișăm un mesaj de eroare
        print(f"Error fetching data: {e}")


# Apelăm funcția pentru a obține și afișa utilizatorii din orașul "Gwenborough"
get_users_data(city_filter="Gwenborough")
