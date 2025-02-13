import json
import requests

# api key/request url
key = "https://api.example.com/data?apikey=your_api_key_here"

data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price']}")
