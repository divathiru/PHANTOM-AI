from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker, declarative_base
from pymongo import MongoClient
from config import POSTGRES_URL, MONGO_URL

# PostgreSQL Connection
engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Threat(Base):
    __tablename__ = "threats"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    data = Column(JSON)

def store_threat(threat):
    db = SessionLocal()
    db.add(Threat(source=threat["source"], data=threat))
    db.commit()
    db.close()

# MongoDB Connection
client = MongoClient(MONGO_URL)
db = client["cybersecurity"]
threats_collection = db["threat_logs"]

def store_raw_threat(threat):
    threats_collection.insert_one(threat)
