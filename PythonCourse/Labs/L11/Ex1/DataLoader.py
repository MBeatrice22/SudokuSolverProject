import pandas as pd

import pandas as pd


def load_sales_data(filepath):
    """Încarcă datele din fișierul CSV și le pregătește pentru analiză"""
    df = pd.read_csv(filepath)

    # Verificăm tipurile de date înainte de conversie
    print("Tipuri de date înainte de conversie:")
    print(df.dtypes)

    # Convertim coloanele corespunzătoare în tipuri numerice
    df['Cantitate'] = pd.to_numeric(df['Cantitate'], errors='coerce')  # Convertim cantitatea în număr
    df['Pret'] = pd.to_numeric(df['Pret'], errors='coerce')  # Convertim prețul în număr

    # Convertim coloana 'Data' la format de dată
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

    # Extragem luna din data pentru analiza pe lună
    df['Luna'] = df['Data'].dt.to_period('M')

    # Verificăm din nou tipurile de date și câteva rânduri
    print("\nTipuri de date după conversie:")
    print(df.dtypes)
    print("\nPrimele 5 rânduri din DataFrame:")
    print(df.head())

    return df


def clean_data(df):
    """Curăță datele: convertim la tip numeric și gestionăm valorile lipsă"""
    df['Cantitate'] = pd.to_numeric(df['Cantitate'], errors='coerce')
    df['Pret'] = pd.to_numeric(df['Pret'], errors='coerce')

    # Înlocuim NaN cu 0
    df['Cantitate'] = df['Cantitate'].fillna(0)
    df['Pret'] = df['Pret'].fillna(0)

    # Creăm o coloană de Venit
    df['Venit'] = df['Cantitate'] * df['Pret']

    return df
