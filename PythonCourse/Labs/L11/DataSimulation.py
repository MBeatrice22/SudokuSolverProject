import numpy as np

def simulate_sales(df, factor=1.1):
    """Simulează vânzări noi pe baza unui factor de multiplicare"""
    df_simulated = df.copy()
    df_simulated['Cantitate'] = df_simulated['Cantitate'] * np.random.uniform(0.8, factor, len(df))
    df_simulated['Venit'] = df_simulated['Cantitate'] * df_simulated['Pret']
    return df_simulated
