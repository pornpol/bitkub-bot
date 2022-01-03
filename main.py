import os
import json

from bitkub import Bitkub
from dotenv import load_dotenv

def print_json(payload):
  print(json.dumps(payload, indent=2))

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

status = bitkub.status()
balance = bitkub.balances()

print_json(balance)


