import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Setarea semintei pentru reproducibilitate
np.random.seed(0)

# Generarea datelor
id_film = np.random.randint(1, 101, size=10000)
id_utilizator = np.random.randint(1, 1001, size=10000)
rating = np.random.randint(1, 6, size=10000)

# Crearea DataFrame-ului
df_ratinguri = pd.DataFrame({
    'ID Utilizator': id_utilizator,
    'ID Film': id_film,
    'Rating': rating
})

# Afișarea primelor 5 linii
df_ratinguri.head()
# Calcularea ratingului mediu pentru fiecare film
rating_mediu_per_film = df_ratinguri.groupby('ID Film')['Rating'].mean()

# Filmele cu mai mult de 50 de evaluări și rating mediu sub 3.5
evaluari_per_film = df_ratinguri.groupby('ID Film').size()
filme_sub_3_5 = rating_mediu_per_film[(evaluari_per_film > 50) & (rating_mediu_per_film < 3.5)]

filme_sub_3_5
# Histogramă pentru toate ratingurile filmelor
plt.figure(figsize=(8, 5))
plt.hist(df_ratinguri['Rating'], bins=np.arange(1, 7)-0.5, edgecolor='black', color='tab:purple')
plt.xlabel('Rating')
plt.ylabel('Frecvență')
plt.title('Distribuția Ratingurilor Filmelor')
plt.xticks(range(1, 6))
plt.grid(True)
plt.tight_layout()
plt.show()

# Top 5 filme cu cel mai mare rating mediu
top_5_filme = rating_mediu_per_film.sort_values(ascending=False).head(5)

# Grafic bară pentru primele 5 filme cu cel mai mare rating mediu
plt.figure(figsize=(8, 5))
top_5_filme.plot(kind='bar', color='tab:blue')
plt.xlabel('ID Film')
plt.ylabel('Rating Mediu')
plt.title('Primele 5 Filme cu Cel Mai Mare Rating Mediu')
plt.tight_layout()
plt.show()

# Scatter plot pentru numărul de evaluări vs. ratingul mediu
evaluari_per_film = df_ratinguri.groupby('ID Film').size()
plt.figure(figsize=(8, 5))
plt.scatter(evaluari_per_film, rating_mediu_per_film, alpha=0.5, color='tab:green')
plt.xlabel('Număr de Evaluări')
plt.ylabel('Rating Mediu')
plt.title('Numărul de Evaluări vs. Ratingul Mediu al Filmelor')
plt.tight_layout()
plt.show()
