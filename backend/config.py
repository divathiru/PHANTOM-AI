import os

# Threat Intelligence API Keys
API_KEYS = {
    "VirusTotal": os.getenv("VIRUSTOTAL_API_KEY"),
    "AbuseIPDB": os.getenv("ABUSEIPDB_API_KEY"),
    "AlienVault": os.getenv("ALIENVAULT_API_KEY"),
}

# Database Config
POSTGRES_URL = "postgresql://user:password@localhost/threat_db"
MONGO_URL = "mongodb://localhost:27017/"

# Kafka & Redis Config
KAFKA_BROKER = "localhost:9092"
REDIS_HOST = "localhost"
