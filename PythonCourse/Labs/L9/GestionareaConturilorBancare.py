class BankAccount:
    def __init__(self, initial_balance=0):
        # Atribut privat pentru sold
        self._balance = initial_balance

    def deposit(self, amount):
        """Adaugă bani în cont."""
        if amount > 0:
            self._balance += amount
        else:
            print("Sumă invalidă pentru depunere.")

    def withdraw(self, amount):
        """Retrage bani din cont, dacă există suficient sold."""
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Fonduri insuficiente pentru retragere.")

    def get_balance(self):
        """Obține soldul actual al contului."""
        return self._balance


# Exemplu de utilizare:
cont = BankAccount(1000)  # Creăm un cont cu soldul inițial de 1000
print(cont.get_balance())  # Afișează soldul curent (1000)

cont.deposit(500)  # Depunem 500 în cont
print(cont.get_balance())  # Afișează soldul curent (1500)

cont.withdraw(200)  # Retragem 200 din cont
print(cont.get_balance())  # Afișează soldul curent (1300)

cont.withdraw(1500)  # Încercăm să retragem mai mult decât soldul
