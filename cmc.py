from coinmarketcap import Market
import json
import requests

url = "https://api.coinmarketcap.com/v1/ticker/bitcoin"

myResponse = requests.get(url)
print (myResponse)

data = myResponse.json()

print (data)
