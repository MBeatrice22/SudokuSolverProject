import requests


def get_exchange_rate(from_currency, to_currency):
    # Cheia API-ului (trebuie să o obții din contul tău de pe Exchangerate-API)
    api_key = "e3a617f459c025337768acb3"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    try:
        # Se face cererea la API pentru a obține cursurile de schimb
        response = requests.get(url)
        data = response.json()

        # Verificăm dacă API-ul a returnat un răspuns valid
        if data["result"] == "success":
            # Extragem cursul de schimb pentru moneda destinatie
            exchange_rate = data["conversion_rates"].get(to_currency)
            if exchange_rate:
                return exchange_rate
            else:
                print(f"Moneda de destinație {to_currency} nu este disponibilă.")
        else:
            print("A apărut o eroare la preluarea datelor de la API.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

    return None


def convert_currency(from_currency, to_currency, amount):
    exchange_rate = get_exchange_rate(from_currency, to_currency)

    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount, exchange_rate
    else:
        return None, None


def main():
    print("Program de conversie valutară")

    # Solicităm utilizatorului să introducă monedele și suma
    from_currency = input("Introduceți moneda de proveniență (ex: USD, EUR, RON): ").upper()
    to_currency = input("Introduceți moneda de destinație (ex: USD, EUR, RON): ").upper()
    amount = float(input("Introduceți suma de convertit: "))

    # Realizăm conversia
    converted_amount, exchange_rate = convert_currency(from_currency, to_currency, amount)

    if converted_amount is not None:
        # Afișăm rezultatul
        print(f"\nConversia: {amount} {from_currency} este echivalentul a {converted_amount:.2f} {to_currency}.")
        print(f"Cursul de schimb actual: 1 {from_currency} = {exchange_rate:.4f} {to_currency}")
    else:
        print("Conversia nu a putut fi realizată. Vă rugăm să verificați monedele introduse.")


if __name__ == "__main__":
    main()
