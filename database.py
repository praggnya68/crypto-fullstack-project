from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///crypto.db")
Base = declarative_base()

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

def save_price(value):
    session = SessionLocal()
    p = Price(price=value)
    session.add(p)
    session.commit()
    session.close()
