numar=int(input("Introduceti un numar: "))
if numar > 1:
    #Dacă numărul este mai mare decât 1,
    # programul verifică dacă există un divizor al acestuia între 2 și (numar-1)
    for i in range(2, numar):
        if numar % i == 0:
            print(f"{numar} nu este un numar prim.")
            break
        else:
            print(f"{numar} este un numar prim.")
            #daca nu se gaseste nici un divizor, nr. este prim
else:
    print(f"{numar} nu este un numar prim.")