from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import apikeys
from collections import defaultdict
from operator import itemgetter
from collections import OrderedDict 
import operator
import nexmo

#binanceCoins = ["Bitcoin","Ethereum","XRP","Polkadot","Cardano","Binance Coin","Litecoin","Chainlink","Bitcoin Cash","Stellar","Dogecoin","USD Coin","Uniswap","Aave","Wrapped Bitcoin","Bitcoin SV","EOS","Monero","Maker","TRON","NEM","Cosmos","Tezos","Synthetix","THETA","Compound","VeChain","Dai","Neo","SushiSwap","UMA","Solana","Elrond","IOTA","Binance USD","FTX Token","Avalanche","Terra","Dash","Filecoin","0x","yearn.finance","Zcash","Decred","Ethereum Classic","Algorand","Kusama","Zilliqa","Waves","Loopring","Ren","NEAR Protocol","Hedera Hashgraph","renBTC","OMG Network","Curve DAO Token","1inch","THORChain","Celo","Ontology","Basic Attention Token","DigiByte","Nano","ICON","BitTorrent","Quant","Alpha Finance Lab","Siacoin","Horizen","Qtum","TrueUSD","Fantom","Stacks","PancakeSwap","IOST","Enjin Coin","Decentraland","Bancor","Ocean Protocol","Bitcoin BEP2","Verge","FunFair","Matic Network","The Graph"]

binanceCoins = ["Bitcoin","Ethereum","XRP","Polkadot","Cardano","Binance Coin","Litecoin","Chainlink","Bitcoin Cash","Stellar","Dogecoin","USD Coin","Uniswap","Aave","Wrapped Bitcoin","Bitcoin SV","EOS","Monero","Maker","TRON","NEM","Cosmos","Tezos","Synthetix","THETA","Compound","VeChain","Dai","Neo","SushiSwap","UMA","Solana","Elrond","Huobi Token","IOTA","Crypto.com Coin","Binance USD","FTX Token","UNUS SED LEO","Avalanche","Terra","Celsius","Dash","Filecoin","0x","yearn.finance","Zcash","Decred","Ethereum Classic","Revain","Algorand","Kusama","Zilliqa","Waves","Loopring","Ren","Nexo","NEAR Protocol","SwissBorg","Hedera Hashgraph","renBTC","OMG Network","Curve DAO Token","1inch","THORChain","Celo","Voyager Token","Ontology","Basic Attention Token","HedgeTrade","DigiByte","Nano","HUSD","ICON","BitTorrent","Quant","Alpha Finance Lab","Siacoin","OKB","Horizen","Ampleforth","Qtum","TrueUSD","Reserve Rights","Kyber Network","Fantom","Stacks","PancakeSwap","IOST","Enjin Coin","Decentraland","Bancor","Ocean Protocol","Bitcoin BEP2","Verge","FunFair","TerraUSD","Matic Network","The Graph"]
timer = 61
limit = 100
phoneNumber = '905301107951'
j=0



while ( j < 99):
    
    firstDict = {}
    secondDict = {}
    rateValues = {}
    print('!!!Basladı!!!')
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':limit,
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikeys.coinmarketAPI,
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    for x in data['data']:
        firstDict[x['name']] = x['quote']['USD']['price']
    

    time.sleep(timer)
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':limit,
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apikeys.coinmarketAPI,
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    for x in data['data']:
        secondDict[x['name']] = x['quote']['USD']['price']
    

    for x in data['data']:
        
        if firstDict.get(x['name']) < secondDict.get(x['name']):
            
            percent = secondDict.get(x['name']) - firstDict.get(x['name'])
            x1 = ((100 * percent) / secondDict.get(x['name']))
            for k in binanceCoins:
                if x['name'] == k:
                    rateValues[x['name']] = x1
                    if(x1 > 0.7):
                        rateo = str(x1)
                        """
                        MSJ = "{} son iki dakikada {}.{}{} oraninda artti! Baslangic Fiyati: {} - Geldigi Fiyat: {}".format(x['name'],rateo[0],rateo[2],rateo[3],firstDict.get(x['name']),secondDict.get(x['name']))
                        
                        client = nexmo.Client(key='9319ed5b', secret='aplrMl4QWgMpXVdW')

                        client.send_message({
                            'from': 'Vonage APIs',
                            'to': phoneNumber,
                            'text': MSJ,
                        })
                        """
                        
                        print("{} - {}.{}{} oraninda artti! Baslangic Fiyati: {} - Geldigi Fiyat: {}".format(x['name'],rateo[0],rateo[2],rateo[3],firstDict.get(x['name']),secondDict.get(x['name'])))
            
        
        """
        elif firstDict.get(x['name']) > secondDict.get(x['name']):
            
            percent2 = firstDict.get(x['name']) - secondDict.get(x['name'])
            x2 = ((100 * percent2) / firstDict.get(x['name']))  
            #if x['name'] == "XRP":
                #rateValues[x['name']] = x2 
        """
            
                     
    j += 1
   
    
    sorted_x = sorted(rateValues.items(), key=operator.itemgetter(1))
    #print(sorted_x)

   
            




