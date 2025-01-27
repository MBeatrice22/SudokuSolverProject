import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Setarea semintei pentru reproducibilitate
np.random.seed(0)

# Generarea datelor pentru 365 de zile
zile = pd.date_range(start="2024-01-01", periods=365, freq="D")
temperatura = np.random.uniform(5, 35, size=365)  # Temperatura între 5°C și 35°C
umiditate = np.random.uniform(30, 90, size=365)   # Umiditatea între 30% și 90%
viteza_vantului = np.random.uniform(0, 20, size=365)  # Viteza vântului între 0 și 20 km/h

# Crearea DataFrame-ului
df_meteo = pd.DataFrame({
    'Data': zile,
    'Temperatura': temperatura,
    'Umiditate': umiditate,
    'Viteza Vantului': viteza_vantului
})

# Calcularea temperaturii resimțite
df_meteo['Temperatura Resimțita'] = df_meteo['Temperatura'] - 0.7 * (df_meteo['Umiditate'] / 100)

# Afișarea primelor 5 linii pentru a verifica datele
df_meteo.head()
# Grafic pentru temperatura și temperatura resimțită
plt.figure(figsize=(10, 6))
plt.plot(df_meteo['Data'], df_meteo['Temperatura'], label='Temperatura', color='tab:red')
plt.plot(df_meteo['Data'], df_meteo['Temperatura Resimțita'], label='Temperatura Resimțita', color='tab:blue')
plt.xlabel('Data')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura și Temperatura Resimțita pe parcursul anului')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calcularea temperaturii medii lunare
df_meteo['Luna'] = df_meteo['Data'].dt.month
temperatura_medie_lunara = df_meteo.groupby('Luna')['Temperatura'].mean()

# Grafic bară pentru temperatura medie lunară
plt.figure(figsize=(8, 5))
temperatura_medie_lunara.plot(kind='bar', color='tab:orange')
plt.xlabel('Luna')
plt.ylabel('Temperatura Medie (°C)')
plt.title('Temperatura Medie Lunara')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()
plt.show()
