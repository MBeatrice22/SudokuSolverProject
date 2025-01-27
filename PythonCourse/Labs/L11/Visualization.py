import matplotlib.pyplot as plt

def plot_most_sold_products(most_sold_df):
    """Crează un grafic cu cele mai vândute produse pe lună"""
    plt.figure(figsize=(10, 6))
    for product in most_sold_df['Produs'].unique():
        product_data = most_sold_df[most_sold_df['Produs'] == product]
        plt.plot(product_data['Luna'].astype(str), product_data['Cantitate'], label=product)
    plt.title('Cele mai vândute produse pe lună')
    plt.xlabel('Luna')
    plt.ylabel('Cantitate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_total_revenue(total_revenue_df):
    """Crează un grafic cu venitul total pe fiecare produs"""
    plt.figure(figsize=(10, 6))
    plt.bar(total_revenue_df['Produs'], total_revenue_df['Venit'], color='skyblue')
    plt.title('Venitul total pe fiecare produs')
    plt.xlabel('Produs')
    plt.ylabel('Venit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_average_monthly_revenue(average_revenue_df):
    """Crează un grafic cu venitul mediu lunar"""
    plt.figure(figsize=(10, 6))
    plt.plot(average_revenue_df['Luna'].astype(str), average_revenue_df['Venit'], marker='o', color='orange')
    plt.title('Venitul mediu lunar')
    plt.xlabel('Luna')
    plt.ylabel('Venit mediu')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
