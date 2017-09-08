import requests
import json

url = 'https://poloniex.com/public?command='


url += 'returnTicker'
r = requests.get(url)
print("I got data")
print(r.json())
'''
data = r.json()

for v in data.keys():
    n = abs(float(data[v]['lowestAsk']) - float(data[v]['highestBid']))
    print("{0} : {1}".format(v, n))
'''

