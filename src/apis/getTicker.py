import json
import requests

import hashlib


url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'
r = requests.get(url)
print(r.json())



url = 'https://www.okcoin.com/api/v1/userinfo.do'
api_key = '31e11009-98b7-4db3-b0f2-c1dd63f72814'
secret_key = 'F3AFD1D8099FB183D38CF171D7086A1D'

headers = {
    "Content-type" : "application/x-www-form-urlencoded"
}

params = {
    'api_key' : api_key,
}
sign = ''
for key in sorted(params.keys()):
    sign += key + '=' + str(params[key]) + '&'

data = sign + 'secret_key=' + secret_key

arrangedSign = hashlib.md5(data.encode('utf-8')).hexdigest().upper()
params['sign'] = arrangedSign

v = requests.post(url, params=params, headers=headers)
print(v.json())


