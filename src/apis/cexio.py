import requests
import json
import time
import hashlib
import hmac


with open("../data/apis.json", 'r') as f:
    api_data = json.load(f)

url = 'https://cex.io/api/balance/'
#url = 'https://cex.io/api/open_orders/'

nonce = str(int(time.time()))
message = nonce + api_data['cexio']['id'] + api_data['cexio']['api_key']

signature = hmac.new(api_data['cexio']['secret_key'].encode('utf-8'),
                    message.encode('utf-8'), digestmod=hashlib.sha256).hexdigest().upper()

payload = {
    'key' : api_data['cexio']['api_key'],
    'signature' : signature,
    'nonce' : nonce
}

headers = {
    'User-agent' : 'bot-cex.io-' + api_data['cexio']['id']
}

print(url)
print(payload)
r = requests.post(url, data=payload)
print(r)
print(r.json())
