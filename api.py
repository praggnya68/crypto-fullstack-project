from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine("sqlite:///crypto.db")


@app.get("/")
def home():
    return {"message": "Crypto API is running"}

@app.get("/current")
def get_current_price():
    df = pd.read_sql("SELECT price FROM prices ORDER BY timestamp DESC LIMIT 1", engine)
    return {"current_price": float(df["price"][0])}

@app.get("/history")
def get_history(limit: int = 50):
    df = pd.read_sql(f"SELECT * FROM prices ORDER BY timestamp DESC LIMIT {limit}", engine)
    return df.to_dict(orient="records")

@app.get("/stats/moving_average")
def moving_average(window: int = 5):
    df = pd.read_sql("SELECT * FROM prices ORDER BY timestamp DESC", engine)
    df = df.head(100)  # use recent data
    df = df.sort_values("timestamp")
    df["ma"] = df["price"].rolling(window).mean()
    return df[["timestamp", "ma"]].dropna().to_dict(orient="records")
