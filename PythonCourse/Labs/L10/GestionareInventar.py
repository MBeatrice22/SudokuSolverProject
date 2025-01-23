class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        """Adaugă un produs în inventar sau actualizează cantitatea acestuia dacă există deja."""
        if cantitate <= 0:
            raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
        if nume in self.produse:
            self.produse[nume] += cantitate
        else:
            self.produse[nume] = cantitate
        print(f"Produsul '{nume}' a fost adăugat cu cantitatea {cantitate}.")

    def cauta_produs(self, nume):
        """Căutăm un produs după nume."""
        if nume in self.produse:
            print(f"Produsul '{nume}' există în inventar cu cantitatea {self.produse[nume]}.")
        else:
            print(f"Eroare: Produsul '{nume}' nu există în inventar.")

    def actualizeaza_cantitate(self, nume, cantitate):
        """Actualizează cantitatea unui produs din inventar."""
        if cantitate <= 0:
            raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
        if nume in self.produse:
            self.produse[nume] = cantitate
            print(f"Cantitatea produsului '{nume}' a fost actualizată la {cantitate}.")
        else:
            print(f"Eroare: Produsul '{nume}' nu există în inventar.")

    def afiseaza_inventar(self):
        """Afișează toate produsele din inventar cu cantitățile lor."""
        if not self.produse:
            print("Inventarul este gol.")
        else:
            print("\nProduse din inventar:")
            for nume, cantitate in self.produse.items():
                print(f"{nume}: {cantitate} bucăți")


def meniu():
    inventar = Inventar()

    while True:
        print("\nMeniu:")
        print("1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Afișează produsele din inventar")
        print("5. Ieși")

        optiune = input("Alege o opțiune (1-5): ")

        if optiune == '1':
            try:
                nume = input("Introdu numele produsului: ")
                cantitate = int(input("Introdu cantitatea produsului: "))
                inventar.adauga_produs(nume, cantitate)
            except ValueError as ve:
                print(f"Eroare: {ve}")
        elif optiune == '2':
            nume = input("Introdu numele produsului pe care vrei să-l cauți: ")
            inventar.cauta_produs(nume)
        elif optiune == '3':
            try:
                nume = input("Introdu numele produsului al cărui cantitate vrei să o actualizezi: ")
                cantitate = int(input("Introdu noua cantitate: "))
                inventar.actualizeaza_cantitate(nume, cantitate)
            except ValueError as ve:
                print(f"Eroare: {ve}")
        elif optiune == '4':
            inventar.afiseaza_inventar()
        elif optiune == '5':
            print("Ieșire din program.")
            break
        else:
            print("Eroare: Opțiune invalidă, te rog să alegi o opțiune între 1 și 5.")


# Lansează programul
meniu()
