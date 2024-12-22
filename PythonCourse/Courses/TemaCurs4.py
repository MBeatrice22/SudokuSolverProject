import re

# Funcție care verifică complexitatea parolei
def verifica_parola(parola):
    feedback = []

    # Verificăm lungimea parolei
    if len(parola) < 8:
        feedback.append("Lipsesc lungimea minimă de 8 caractere.")

    # Verificăm dacă conține litere majuscule
    if not any(c.isupper() for c in parola):
        feedback.append("Lipsesc litere majuscule.")

    # Verificăm dacă conține litere minuscule
    if not any(c.islower() for c in parola):
        feedback.append("Lipsesc litere minuscule.")

    # Verificăm dacă conține cifre
    if not any(c.isdigit() for c in parola):
        feedback.append("Lipsesc cifre.")

    # Verificăm dacă conține caractere speciale
    if not any(c in "!@#$%^&*()-_+=<>?" for c in parola):
        feedback.append("Lipsesc caractere speciale.")

    # Verificăm dacă parola conține spații
    if ' ' in parola:
        feedback.append("Parola nu trebuie să conțină spații.")

    # Dacă feedback-ul este gol, parola este puternică
    if len(feedback) == 0:
        return "Parola dvs. este puternică."
    else:
        return "Parola dvs. este slabă.\n" + "\n".join(feedback)


# Funcție principală pentru procesarea parolelor
def proceseaza_parole():
    # Solicităm utilizatorului să introducă parolele, separate prin virgulă
    parole_input = input("Introduceți parolele (separate prin virgulă): ")

    # Împărțim parolele într-o listă, eliminând spațiile inutile
    parole = [parola.strip() for parola in parole_input.split(',')]

    # Procesăm fiecare parolă și afișăm rezultatele
    for parola in parole:
        print(f"\nParola: {parola}")
        print(verifica_parola(parola))

# Apelăm funcția principală
proceseaza_parole()
