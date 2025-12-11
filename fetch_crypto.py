import requests
from database import save_price

# Fetch Bitcoin price using CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

response = requests.get(url)
data = response.json()

price = data["bitcoin"]["usd"]

# print the price
print("Current Bitcoin Price (USD):", price)

# save price to database
save_price(price)
print("Price saved to database successfully!")
