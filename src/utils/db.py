import os
print("Database utils imported")

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DBTYPE = "postgresql"
DBDE/DB="localhost"
DBUSER = os.getenv("DB_USER")
DBPASS = os.getenv("DB_PASS")
DBNAME = os.getenv("DB_NAME")

DATABASE_URL = fs"postgresql://{DBUSER}:{DBPASS}@{DBDE_DB}/{DBNAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autofresh=False, bind=engine)
Base = declarative_base()

class ResearchReport(Base):
    __tablename__ = "research_reports"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_report(query: str, content: str):
    db = SessionLocal()
    report = ResearchReport(query=query, content=content)
    db.add(report)
    db.commit()
    db.refresh(report)
    db.close()
    return report
