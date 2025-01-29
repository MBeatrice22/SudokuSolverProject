import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setăm seed pentru reproducibilitate
np.random.seed(42)

# Numărul de zile pentru simulare
numar_zile = 60

# Generăm datele pentru vânzări (aceleași pași din exemplul anterior)
produse_vandute_per_zi = np.random.randint(5, 16, size=numar_zile)
preturi = np.random.normal(loc=40, scale=8, size=numar_zile)
cantitati_vandute = np.random.randint(1, 11, size=numar_zile)
promoții = np.random.rand(numar_zile) < 0.3
preturi[promoții] *= 0.8
total_vanzari_per_zi = preturi * cantitati_vandute
profit_per_zi = total_vanzari_per_zi * 0.30

# Creăm DataFrame-ul pentru datele de vânzări
date_vanzari = pd.DataFrame({
    'Ziua': np.arange(1, numar_zile + 1),
    'Produse_vandute': produse_vandute_per_zi,
    'Pret_unitar': preturi,
    'Cantitate_vanduta': cantitati_vandute,
    'Total_vanzari': total_vanzari_per_zi,
    'Profit': profit_per_zi,
    'Promoție': promoții
})

# 1. Evoluția veniturilor și profitului pe zile
# Extragem venitul total și profitul total
venituri = date_vanzari[['Ziua', 'Total_vanzari']]
profituri = date_vanzari[['Ziua', 'Profit']]

# Vizualizare evoluția veniturilor și profitului
plt.figure(figsize=(10, 6))
plt.plot(venituri['Ziua'], venituri['Total_vanzari'], label='Venituri', color='blue', linestyle='-')
plt.plot(profituri['Ziua'], profituri['Profit'], label='Profit', color='green', linestyle='--')
plt.title('Evoluția veniturilor și profitului pe zile')
plt.xlabel('Ziua')
plt.ylabel('Valoare')
plt.legend()
plt.grid(True)
plt.show()

# 2. Distribuția prețurilor și cantităților vândute
plt.figure(figsize=(10, 6))

# Histogramă pentru prețuri
plt.subplot(1, 2, 1)
sns.histplot(date_vanzari['Pret_unitar'], kde=True, color='blue', bins=15)
plt.title('Distribuția prețurilor')

# Histogramă pentru cantitățile vândute
plt.subplot(1, 2, 2)
sns.histplot(date_vanzari['Cantitate_vanduta'], kde=True, color='orange', bins=10)
plt.title('Distribuția cantităților vândute')

plt.tight_layout()
plt.show()

# 3. Vizualizarea promoțiilor
# Identificăm zilele cu promoție
zile_promotii = date_vanzari[date_vanzari['Promoție'] == True]

# Calculăm impactul promoțiilor asupra prețurilor (comparăm prețul înainte și după promoție)
impact_promo = zile_promotii[['Ziua', 'Pret_unitar']].copy()
impact_promo['Pret_initial'] = impact_promo['Pret_unitar'] / 0.8  # Restabilim prețul inițial
impact_promo['Reducere'] = impact_promo['Pret_initial'] - impact_promo['Pret_unitar']
impact_promo['Reducere_procentuala'] = (impact_promo['Reducere'] / impact_promo['Pret_initial']) * 100

# Vizualizăm impactul promoțiilor asupra prețurilor
plt.figure(figsize=(10, 6))
plt.bar(impact_promo['Ziua'], impact_promo['Reducere_procentuala'], color='red')
plt.title('Impactul promoțiilor asupra prețurilor')
plt.xlabel('Ziua')
plt.ylabel('Reducere procentuală')
plt.grid(True)
plt.show()
