import time
import requests
from database import save_price

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

while True:
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]

    print("BTC Price:", price)
    save_price(price)
    print("Saved to database.\n")

    time.sleep(300)  # wait 5 minutes
