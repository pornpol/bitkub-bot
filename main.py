import os
import json
import time
import requests

from colorama import Fore
from bitkub import Bitkub
from dotenv import load_dotenv

load_dotenv()

def print_json(payload):
  print(json.dumps(payload, indent=2))

def line_notify(message, token):
  url = 'https://notify-api.line.me/api/notify'
  headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + token
  }

  r = requests.post(url, headers=headers, data = {'message':message})
  return r

# Get values from .env
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
LINE_NOTIFY_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')

coins = os.getenv('COINS').split(' ')

# Initialize Bitkub
bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

# balance = bitkub.balances()
last_prices = {}

history = bitkub.tradingview(sym='BTC_THB', int=1, frm=1633424427, to=1633427427)
print_json(history)

# Forever loop with 1 second sleep
while True:
  prices = bitkub.ticker()

  for coin in coins:
    price = prices[coin]["last"]
    color = Fore.WHITE

    if price > last_prices.get(coin, 0):
      color = Fore.GREEN
    elif price < last_prices.get(coin, 0):
      color = Fore.RED

    print(color + coin + ': ' + str(price))
    last_prices[coin] = price

    # line_notify(str(btc_price), LINE_NOTIFY_TOKEN)

  time.sleep(10) # 1 second
  print('')


