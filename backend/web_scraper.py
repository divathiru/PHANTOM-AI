import requests
from bs4 import BeautifulSoup

BLOG_URLS = [
    "https://www.bleepingcomputer.com/",
    "https://thehackernews.com/",
]

def scrape_threat_blogs():
    scraped_data = []
    for url in BLOG_URLS:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            title = article.find("h2").text if article.find("h2") else "No Title"
            link = article.find("a")["href"] if article.find("a") else "No Link"
            scraped_data.append({"title": title, "link": link})
    
    return scraped_data
