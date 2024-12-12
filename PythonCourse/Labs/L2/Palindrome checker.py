sir = input("Introdu un cuvânt: ")

# Verificăm dacă cuvântul este palindrom
este_palindrom = True
for i in range(len(sir) // 2): #compari caracterele de la început cu cele de la sfârșit,
    # începând cu capetele și înaintând spre mijloc,
    # atunci trebuie să verificam doar primele n // 2 caractere

    if sir[i] != sir[len(sir) - 1 - i]: #verifică dacă litera de la poziția i este diferita de caracterul de la poziția opusă
        este_palindrom = False
        break

if este_palindrom:
    print("Este un palindrom!")
else:
    print("Nu este un palindrom.")