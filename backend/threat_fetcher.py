import requests
from config import API_KEYS

THREAT_APIS = {
    "VirusTotal": "https://www.virustotal.com/api/v3/intelligence",
    "AbuseIPDB": "https://api.abuseipdb.com/api/v2/check",
}

HEADERS = {
    "VirusTotal": {"x-apikey": API_KEYS["VirusTotal"]},
    "AbuseIPDB": {"Key": API_KEYS["AbuseIPDB"]},
}

def fetch_threat_data():
    threats = []
    for name, url in THREAT_APIS.items():
        response = requests.get(url, headers=HEADERS[name])
        if response.status_code == 200:
            threats.append(response.json())
    return threats
