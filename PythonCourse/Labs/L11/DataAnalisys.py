import pandas as pd

def most_sold_products_per_month(df):
    """Afișează cele mai vândute produse pe lună"""
    df['Luna'] = pd.to_datetime(df['Data']).dt.to_period('M')
    most_sold = df.groupby(['Luna', 'Produs'])['Cantitate'].sum().reset_index()
    return most_sold

def total_revenue_per_product(df):
    """Afișează venitul total pe fiecare produs"""
    total_revenue = df.groupby('Produs')['Venit'].sum().reset_index()
    return total_revenue

def filter_sales_by_date(df, start_date, end_date):
    """Filtrează vânzările între două date"""
    df['Data'] = pd.to_datetime(df['Data'])
    filtered_sales = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]
    return filtered_sales

def average_monthly_revenue(df):
    """Afișează venitul mediu lunar"""
    df['Luna'] = pd.to_datetime(df['Data']).dt.to_period('M')
    average_revenue = df.groupby('Luna')['Venit'].mean().reset_index()
    return average_revenue
