import requests
import json
import time
import hashlib
import hmac

f = open("apis.json", 'r')
apis_data = json.load(f)
f.close()


url = "https://api.bitfinex.com/v1/pubticker/iotaBTC"

r = requests.get(url)
print(r.json())

