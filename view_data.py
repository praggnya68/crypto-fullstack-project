from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///crypto.db")

df = pd.read_sql("SELECT * FROM prices ORDER BY timestamp DESC", engine)

print(df)
