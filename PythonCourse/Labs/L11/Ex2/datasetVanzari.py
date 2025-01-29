import numpy as np
import pandas as pd

# Setăm seed pentru reproducibilitatea rezultatelor
np.random.seed(42)

# Numărul de zile pentru simulare
numar_zile = 60

# 1. Generarea numărului de produse vândute pe fiecare zi (între 5 și 15 produse pe zi)
produse_vandute_per_zi = np.random.randint(5, 16, size=numar_zile)

# 2. Generarea prețurilor produselor folosind o distribuție normală (în jurul valorii de 40, cu deviație standard de 8)
preturi = np.random.normal(loc=40, scale=8, size=numar_zile)

# 3. Generarea cantităților vândute per produs (între 1 și 10 unități per produs)
cantitati_vandute = np.random.randint(1, 11, size=numar_zile)

# 4. Generarea promoțiilor: probabilitatea de 30% ca prețul să scadă cu 20% pe anumite zile
promoții = np.random.rand(numar_zile) < 0.3  # Probabilitate 30% pentru promoție
preturi[promoții] *= 0.8  # Reducerea prețului cu 20% pentru zilele cu promoție

# 5. Calculul totalului vânzărilor per zi (preț unitar * cantitate vândută)
total_vanzari_per_zi = preturi * cantitati_vandute

# 6. Calculul profitului per zi: marja de profit este 30% din prețul de vânzare
profit_per_zi = total_vanzari_per_zi * 0.30

# Crearea unui DataFrame pentru a organiza datele
date_vanzari = pd.DataFrame({
    'Ziua': np.arange(1, numar_zile + 1),
    'Produse_vandute': produse_vandute_per_zi,
    'Pret_unitar': preturi,
    'Cantitate_vanduta': cantitati_vandute,
    'Total_vanzari': total_vanzari_per_zi,
    'Profit': profit_per_zi
})

# Afișăm primele 10 zile din dataset pentru a verifica datele
print(date_vanzari.head(10))
