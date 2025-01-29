import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# Funcție pentru a obține prețurile criptomonedelor Bitcoin și Ethereum
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifică dacă cererea a fost cu succes
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        ethereum_price = data['ethereum']['usd']
        return bitcoin_price, ethereum_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto prices: {e}")
        return None, None


# Funcție pentru a extrage cele mai recente 5 știri de pe CoinDesk
def get_latest_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifică dacă cererea a fost cu succes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Căutăm titlurile articolelor din site-ul CoinDesk
        headlines = soup.find_all('a', class_='card-title', limit=5)  # Limităm la 5 știri

        news = []
        for headline in headlines:
            title = headline.get_text(strip=True)
            link = headline.get('href')
            if link:
                news.append((title, f"https://www.coindesk.com{link}"))

        return news
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []


# Funcție pentru a afișa prețurile criptomonedelor într-un tabel
def display_crypto_prices(bitcoin_price, ethereum_price):
    data = [
        ["Bitcoin", bitcoin_price],
        ["Ethereum", ethereum_price]
    ]
    print("Cripto-monede Prețuri (USD):")
    print(tabulate(data, headers=["Cripto-moneda", "Preț (USD)"], tablefmt="grid"))
    print()


# Funcție pentru a afișa ultimele 5 știri
def display_news(news):
    print("Ultimele 5 știri de pe CoinDesk:")
    for i, (title, link) in enumerate(news, 1):
        print(f"{i}. {title} - {link}")
    print()


def main():
    # Obținem prețurile criptomonedelor
    bitcoin_price, ethereum_price = get_crypto_prices()
    if bitcoin_price is not None and ethereum_price is not None:
        # Afișăm prețurile criptomonedelor
        display_crypto_prices(bitcoin_price, ethereum_price)

    # Obținem ultimele 5 știri
    news = get_latest_news()
    if news:
        # Afișăm știrile
        display_news(news)


if __name__ == "__main__":
    main()
