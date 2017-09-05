import requests
import json
import time
import hashlib
import hmac

f = open("apis.json", 'r')
apis_data = json.load(f)
f.close()

url = 'https://cex.io/api/balance/'
#url = 'https://cex.io/api/open_orders/'

nonce = str(int(time.time()))
message = nonce + apis_data['cexio']['id'] + apis_data['cexio']['api_key']

signature = hmac.new(apis_data['cexio']['secret_key'].encode('utf-8'),
                    message.encode('utf-8'), digestmod=hashlib.sha256).hexdigest().upper()

payload = {
    'key' : apis_data['cexio']['api_key'],
    'signature' : signature,
    'nonce' : nonce
}

headers = {
    'User-agent' : 'bot-cex.io-' + apis_data['cexio']['id']
}

print(url)
print(payload)
r = requests.post(url, data=payload)
print(r)
print(r.json())
