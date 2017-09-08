import requests
import json
import time
import hashlib
import hmac
from urllib.parse import urlencode


'''
url = 'https://yobit.net/api/2/eth_btc/ticker'

r = requests.get(url)
print(r.json())
'''

with open('../data/apis.json', 'r') as f:
    data = json.load(f)


url = 'https://yobit.net/tapi'
values = {}
values['method'] = 'getInfo'
values['nonce'] = str(int(time.time()))
body = urlencode(values)
signature = hmac.new(data['yobit']['secret_key'].encode('utf-8'), body.encode('utf-8'), hashlib.sha512).hexdigest()

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Key' : data['yobit']['api_key'],
    'Sign' : signature
}

req = requests.post(url, data=values, headers=headers)
print(req)
print(req.json())



