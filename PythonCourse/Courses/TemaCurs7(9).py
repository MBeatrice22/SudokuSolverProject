# Clasa Carte
class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        return f"{self.titlu} de {self.autor} (ISBN: {self.isbn})"

# Clasa MembruBiblioteca
class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if carte.este_imprumutata:
            print(f"Cartea '{carte.titlu}' este deja împrumutată.")
        else:
            self.carti_imprumutate.append(carte)
            carte.este_imprumutata = True
            print(f"{self.nume} a împrumutat cartea '{carte.titlu}'.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            self.carti_imprumutate.remove(carte)
            carte.este_imprumutata = False
            print(f"{self.nume} a returnat cartea '{carte.titlu}'.")
        else:
            print(f"{self.nume} nu a împrumutat cartea '{carte.titlu}'.")

# Clasa Biblioteca
class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea '{carte.titlu}' a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea '{carte.titlu}' nu se află în bibliotecă.")

    def listeaza_carti_disponibile(self):
        disponibile = [carte for carte in self.carti if not carte.este_imprumutata]
        if disponibile:
            print("Cărțile disponibile în bibliotecă:")
            for carte in disponibile:
                print(carte)
        else:
            print("Nu există cărți disponibile în bibliotecă.")

# Crearea cărților
carte1 = Carte("1984", "George Orwell", "1234567890")
carte2 = Carte("Mândrie și prejudecată", "Jane Austen", "9876543210")
carte3 = Carte("Micul prinț", "Antoine de Saint-Exupéry", "1112131415")
carte4 = Carte("Harry Potter și piatra filosofală", "J.K. Rowling", "2222334455")
carte5 = Carte("Frankenstein", "Mary Shelley", "3333445566")

# Crearea membrilor
membru1 = MembruBiblioteca("Ion Popescu")
membru2 = MembruBiblioteca("Maria Ionescu")
membru3 = MembruBiblioteca("Andrei Georgescu")

# Crearea bibliotecii și adăugarea cărților
biblioteca = Biblioteca()
biblioteca.adauga_carte(carte1)
biblioteca.adauga_carte(carte2)
biblioteca.adauga_carte(carte3)
biblioteca.adauga_carte(carte4)
biblioteca.adauga_carte(carte5)

# Listarea cărților disponibile
biblioteca.listeaza_carti_disponibile()

# Împrumutarea și returnarea cărților
membru1.imprumuta_carte(carte1)
membru2.imprumuta_carte(carte1)  # Această carte este deja împrumutată, deci nu poate fi împrumutată de al doilea membru

membru2.imprumuta_carte(carte2)
membru3.imprumuta_carte(carte2)  # Această carte este deja împrumutată, deci nu poate fi împrumutată de al treilea membru

biblioteca.listeaza_carti_disponibile()

membru1.returneaza_carte(carte1)
membru3.imprumuta_carte(carte2)

# Listarea cărților disponibile după returnare
biblioteca.listeaza_carti_disponibile()
