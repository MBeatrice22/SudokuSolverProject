# Datele de intrare
preturi_produse = {"mere": 2.0, "kiwi": 3.5, "avocado": 5.5, "mango": 4.5}
stoc_initial = {"mere": 10, "kiwi": 20, "avocado": 15, "mango": 5}
vanzari = [("mere", 8), ("kiwi", 11), ("avocado", 10), ("mango", 2)]
venit_total = 0.0 #Calcularea venitului total și actualizarea stocului
stocuri_raman = stoc_initial.copy()  # copiem stocul initial pentru a-l actualiza
for produs, cantitate_vanduta in vanzari:
    if produs in preturi_produse:
        venit_total += preturi_produse[produs] * cantitate_vanduta #Calculăm venitul din vânzare pentru produsul curent
        stocuri_raman[produs] -= cantitate_vanduta #Actualizăm stocul
#Identificăm produsele ce trebuie realimentate
produse_realimentare = {produs for produs, cantitate in stocuri_raman.items() if cantitate < 5}
print(f"Venit total: {venit_total} RON") #Generarea raportului
print("Stocuri rămase:")
for produs, stoc in stocuri_raman.items():
    print(f"  - {produs}: {stoc}")
print("Produse ce necesită realimentare:")
for produs in produse_realimentare:
    print(f"  - {produs}")
