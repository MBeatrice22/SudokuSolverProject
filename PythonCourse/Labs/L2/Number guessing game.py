import random

# Programul generează un număr aleatoriu între 1 și 100
numar_secret = random.randint(1, 100)

while True: #se creeaza o bucla infinita care se va parcurge pana la ghicirea numarului
    numar_user = int(input("Ghicește numărul între 1 și 100: ")) #utilizatorul introduce un numar
    # Verificăm dacă numărul introdus este corect
    if numar_user < numar_secret:
        print("Prea mic! Mai încearcă.")
    elif numar_user > numar_secret:
        print("Prea mare! Mai încearcă.")
    else:
        print("Felicitări! Ai ghicit numărul.")
        break