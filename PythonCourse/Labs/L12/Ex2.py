import requests


# Funcția pentru a obține informațiile meteo
def get_weather(city):
    try:
        # Trimite cererea GET către API-ul wttr.in pentru orașul specificat
        response = requests.get(f'https://wttr.in/{city}?format=%C+%t+%w', verify=False)

        # Verificăm dacă API-ul a returnat un răspuns valid
        if response.status_code != 200:
            print(f"Eroare la conectarea la API sau orașul nu a fost găsit. Status code: {response.status_code}")
            return

        # Prelucrăm răspunsul
        weather_info = response.text.strip()

        # Dacă nu există date meteo (ex: orașul nu a fost găsit)
        if "unknown location" in weather_info:
            print("Orașul nu a fost găsit. Vă rugăm să încercați un alt oraș.")
            return

        # Afișăm informațiile meteo
        print(f"Informatii meteo pentru {city}:")
        print(weather_info)

    except requests.exceptions.RequestException as e:
        # Gestionăm erorile de conexiune, incluzând erori SSL
        print(f"Eroare la conectarea la API: {e}")


# Solicităm utilizatorului să introducă un oraș
city = input("Introduceți numele unui oraș pentru a obține informațiile meteo: ")
get_weather(city)
