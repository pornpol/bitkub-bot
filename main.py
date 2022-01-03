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
  headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

  r = requests.post(url, headers=headers, data = {'message':message})
  return r.text

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

LINE_NOTIFY_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')

bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

balance = bitkub.balances()

last_btc_price = bitkub.ticker(sym='THB_BTC')["THB_BTC"]["last"]

while True:
  btc_price = bitkub.ticker(sym='THB_BTC')["THB_BTC"]["last"]
  color = Fore.WHITE

  if btc_price > last_btc_price:
    color = Fore.GREEN
  elif btc_price < last_btc_price:
    color = Fore.RED

  print(color + str(btc_price))
  # line_notify(str(btc_price), LINE_NOTIFY_TOKEN)

  last_btc_price = btc_price
  time.sleep(1) # 1 second


