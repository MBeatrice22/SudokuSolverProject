import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Setarea semintei pentru reproducibilitate
np.random.seed(0)

# Generarea datelor pentru 730 de zile
zile = pd.date_range(start="2023-01-01", periods=730, freq="D")
pret_initial = 100  # Prețul inițial al acțiunii
schimbari_procentuale = np.random.normal(loc=0, scale=0.02, size=730)  # Schimbări procentuale zilnice

# Calcularea prețului de închidere zilnic
preturi_inchidere = pret_initial * (1 + schimbari_procentuale).cumprod()

# Crearea DataFrame-ului
df_actiuni = pd.DataFrame({
    'Data': zile,
    'Schimbare Zilnica (%)': schimbari_procentuale * 100,
    'Pret de Închidere': preturi_inchidere
})

# Calcularea prețului cumulativ
df_actiuni['Pret Cumulativ'] = df_actiuni['Pret de Închidere'].cumprod()

# Afișarea primelor 5 linii
df_actiuni.head()
# Calcularea mediilor mobile
df_actiuni['Media Mobila 30 Zile'] = df_actiuni['Pret de Închidere'].rolling(window=30).mean()
df_actiuni['Media Mobila 100 Zile'] = df_actiuni['Pret de Închidere'].rolling(window=100).mean()

# Identificarea perioadelor în care prețul acțiunilor a fost peste media mobilă de 100 de zile
perioade_peste_media_mobila = df_actiuni[df_actiuni['Pret de Închidere'] > df_actiuni['Media Mobila 100 Zile']]

perioade_peste_media_mobila.head()


# Grafic pentru prețul de închidere zilnic și mediile mobile
plt.figure(figsize=(12, 6))
plt.plot(df_actiuni['Data'], df_actiuni['Pret de Închidere'], label='Preț de Închidere', color='tab:blue')
plt.plot(df_actiuni['Data'], df_actiuni['Media Mobila 30 Zile'], label='Media Mobilă 30 Zile', color='tab:orange')
plt.plot(df_actiuni['Data'], df_actiuni['Media Mobila 100 Zile'], label='Media Mobilă 100 Zile', color='tab:green')
plt.fill_between(df_actiuni['Data'], df_actiuni['Pret de Închidere'], df_actiuni['Media Mobila 100 Zile'], where=(df_actiuni['Pret de Închidere'] > df_actiuni['Media Mobila 100 Zile']), color='lightgreen', alpha=0.5, label='Peste Media Mobila 100 Zile')
plt.xlabel('Data')
plt.ylabel('Preț Acțiune ($)')
plt.title('Prețul Acțiunii și Mediile Mobile')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
