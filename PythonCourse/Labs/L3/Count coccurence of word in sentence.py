# Citirea propoziției și a cuvântului de la tastatura
propozitie = input("Introdu o propoziție: ")
cuvant = input("Introdu cuvântul pe care vrei să-l cauți: ")

# Numără exact de cate ori apare cuvântul introdus în propoziția dată, inclusiv facand distincția între litere mari și mici.
aparitii = propozitie.count(cuvant)

# Afișează rezultatul
print(f"Cuvântul '{cuvant}' apare de {aparitii} ori în propoziția dată.")
