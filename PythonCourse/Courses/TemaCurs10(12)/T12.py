import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code}")
        return None

def extract_articles(url):
    html = get_html(url)
    if html is None:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    articles = []

    # Căutăm toate articolele de pe HotNews.ro
    for article in soup.find_all('article'):
        title = article.find('h2')
        if title:
            title_text = title.get_text(strip=True)
        else:
            continue

        link = article.find('a', href=True)
        full_url = link['href'] if link else 'Nu există link'

        # Adăugăm titlul și URL-ul în lista de articole
        articles.append({
            'title': title_text,
            'url': full_url
        })

    return articles

def save_articles_to_csv(articles, filename="articles.csv"):
    keys = articles[0].keys() if articles else ["title", "url"]
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

# URL-ul de test
url = "https://hotnews.ro/"
articles = extract_articles(url)
save_articles_to_csv(articles)

print("Articolele au fost salvate cu succes!")
