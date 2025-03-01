from celery import Celery
from threat_fetcher import fetch_threat_data
from web_scraper import scrape_threat_blogs
from database import store_threat

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def scheduled_fetch():
    threats = fetch_threat_data()
    blogs = scrape_threat_blogs()
    
    for threat in threats:
        store_threat(threat)
    
    for blog in blogs:
        store_threat({"source": "Cybersecurity Blog", "data": blog})
