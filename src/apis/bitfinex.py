import requests
import json
import time
import hashlib
import hmac
from datetime import datetime

f = open("../data/apis.json", 'r')
apis_data = json.load(f)
f.close()


'''
url = "https://api.bitfinex.com/v1/pubticker/iotaBTC"

r = requests.get(url)
print(r.json())
'''


url = "https://api.bitfinex.com/v1/pubticker/"




def getTicker(pair):
    url = "https://api.bitfinex.com/v1/pubticker/"

    url += pair

    r = requests.get(url)
    print(r.json())
    return r.json()


'''
def initJsonFile():
    data = getTicker('btcusd')
    fixedData = {}
    fixedData['count'] = 0
    
    tmpData = {}
    tmpData[0] = data
    fixedData['btcusd'] = tmpData
    
    with open('Ticker_bitfinex.json', 'w') as w:
        json.dump(fixedData, w, sort_keys=True, indent=4)
'''

def main():
    data = getTicker('btcusd')
    with open('../data/Ticker_bitfinex.json', 'r') as g:
        fileData = json.load(g)
        

    fixedData = {}
    fixedData['count'] = (str(int(fileData['count']) + 1))

    tmpData = fileData['btcusd']

    tmpData[str(int(fileData['count'])+1)] = data

    fixedData['btcusd'] = tmpData

    with open('../data/Ticker_bitfinex.json', 'w') as w:

        json.dump(fixedData, w, sort_keys=True, indent=4)

if __name__ == "__main__":
    main()

        
        


    
