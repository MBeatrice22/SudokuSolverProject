import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# Funcție pentru a obține prețurile Bitcoin și Ethereum
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Va ridica o excepție dacă cererea a eșuat
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        ethereum_price = data['ethereum']['usd']
        return bitcoin_price, ethereum_price
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare la obținerea prețurilor criptomonedelor: {e}")
        return None, None


# Funcție pentru a obține ultimele 5 știri de pe CoinDesk
def get_coin_desk_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Căutăm link-uri ce conțin știri (fiecare link asociat cu un titlu de știre)
        news_items = soup.find_all('a', href=True)  # Căutăm toate link-urile din pagină
        news = []

        # Iterăm prin link-uri și selectăm doar cele care sunt știri
        for item in news_items:
            title = item.get_text()
            link = item['href']
            if title and link:
                # Verificăm dacă link-ul este valid și îl completăm cu domeniul coindesk.com
                full_link = "https://www.coindesk.com" + link if not link.startswith('http') else link
                news.append([title.strip(), full_link])

            if len(news) >= 5:  # Ne oprim după ce am obținut 5 știri
                break

        return news
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare la obținerea știrilor de pe CoinDesk: {e}")
        return []


# Funcție principală pentru a rula scriptul
def main():
    print("Program de preluare prețuri criptomonede și știri\n")

    # Obținem prețurile criptomonedelor
    bitcoin_price, ethereum_price = get_crypto_prices()
    if bitcoin_price is None or ethereum_price is None:
        print("Nu s-au putut obține prețurile criptomonedelor.")
        return

    # Afișăm prețurile într-un tabel
    crypto_data = [["Bitcoin", bitcoin_price], ["Ethereum", ethereum_price]]
    print("Prețuri criptomonede (în USD):")
    print(tabulate(crypto_data, headers=["Moneda", "Preț (USD)"], tablefmt="fancy_grid"))

    # Obținem ultimele 5 știri de pe CoinDesk
    news = get_coin_desk_news()
    if not news:
        print("\nNu s-au putut obține știrile.")
        return

    # Afișăm știrile într-un format lizibil
    print("\nUltimele 5 știri de pe CoinDesk:")
    for index, (title, link) in enumerate(news, 1):
        print(f"{index}. {title}\n   Link: {link}\n")


if __name__ == "__main__":
    main()
