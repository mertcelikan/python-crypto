from binance.client import Client
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import apikeys

client = Client(apikeys.binanceAPI, apikeys.binanceKEY
)

#bakiyemizi ogrenmek icin
balance = client.get_asset_balance(asset='USDT')

#satn alim
buyOrder = client.order_market_buy(symbol='DOTUSDT', quantity = 0.01)

#satis
sellOrder = client.order_market_sell(symbol='ETHUSDT', quantity = 0.011)

#su fiyat artarsa sat
order = client.order_limit_sell(
    symbol='XRPUSDT',
    quantity= 0.02,
    price='0.35')

#su fiyata duserse al
order = client.order_limit_buy(
    symbol='XRPUSDT',
    quantity=1,
    price='0.30')



