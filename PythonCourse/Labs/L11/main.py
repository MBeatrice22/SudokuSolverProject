from DataLoader import load_sales_data, clean_data
from DataAnalisys import most_sold_products_per_month, total_revenue_per_product, filter_sales_by_date, average_monthly_revenue
from DataSimulation import simulate_sales
from Visualization import plot_most_sold_products, plot_total_revenue, plot_average_monthly_revenue

def main():
    # Încarcă și curăță datele
    df = load_sales_data('vanzari.csv')
    df = clean_data(df)

    # Analizează cele mai vândute produse pe lună
    most_sold_df = most_sold_products_per_month(df)
    print("Cele mai vândute produse pe lună:")
    print(most_sold_df)
    plot_most_sold_products(most_sold_df)

    # Analizează venitul total pe fiecare produs
    total_revenue_df = total_revenue_per_product(df)
    print("Venitul total pe fiecare produs:")
    print(total_revenue_df)
    plot_total_revenue(total_revenue_df)

    # Analizează venitul mediu lunar
    average_revenue_df = average_monthly_revenue(df)
    print("Venitul mediu lunar:")
    print(average_revenue_df)
    plot_average_monthly_revenue(average_revenue_df)

    # Simulează vânzările
    simulated_df = simulate_sales(df, factor=1.2)
    print("Simularea vânzărilor (vânzări estimate cu factor 1.2):")
    print(simulated_df[['Produs', 'Cantitate', 'Pret', 'Venit']])

if __name__ == '__main__':
    main()
