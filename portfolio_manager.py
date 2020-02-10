from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from endpoint_caller import endpointCaller
import time
import csv

LATESTURL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
HEADERS = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '85b403c5-f580-4b25-87dc-a88de76e0bf9',
}


class portfolioManager():
    def __init__(self):
        self.callerId = 1
        self.top10Data = {}
    # The parameters into this method will have to be devised and sent from elsewhere
    def getCryptoData(self, session, url, parameters):
        endpointCall = endpointCaller()
        top10List = endpointCall.getTop10(session, url, parameters)
        data = {}
        for x in top10List['data']:
            newDict = {}
            newDict['name'] = x['name']
            symbol = x['symbol']
            newDict['symbol'] = symbol
            newDict['price'] = x['quote']['USD']['price']
            newDict['percentChange24h'] = x['quote']['USD']['percent_change_24h']
            newDict['perecentChange7d'] = x['quote']['USD']['percent_change_7d']
            newDict['marketCap'] = x['quote']['USD']['market_cap']
            data[symbol] = newDict
        self.top10Data = data
        return data

def parameters(start, limit):
    parameters = {
    # Where to start from in the list that the API wants to return
    'start':start,
    # Until what index of the list being returned
    'limit':limit,
    # I can always change this but it's easier to start with USD
    'convert':'USD'
    }
    return parameters

def getPortfolio():
    with open('portfolio.txt') as csv_file:
        csv_reader = csv_file.readlines()
        symbolList = csv_reader[0].split(',')
        priceList = csv_reader[1].split(',')
        portfolio = {}
        for x,y in zip(symbolList, priceList):
            if x != '':
                portfolio[x.strip('\n')] =y
        print("Returning portfolio ", portfolio)
        return portfolio

def printChoices():
    print("What would you like to do? ")
    print("1. View top 10")
    print("2. Add to holding")

def topTen(response):
    #print("Name: " + "Symbol: " + 'Price ' + "Percent change 24 hours " + 'Percent change 7 days')
    length = 0
    size_of_space = 14
    size_of_space_symbol = 8
    for length,symbol in enumerate(response,1):
        if length == 10:
            return response
        coin = response[symbol]
        price = coin['price']
        price = str(price)
        if price[0] == '0':
            price = float(price)
            price = round(price,5)
        else:
            price = float(price)
            price = round(price,2)
        price = str(price)
        white_space = ' ' * 20
        size_of_space_missing_coin = (size_of_space - len(coin['name'])) * ' '
        size_of_space_missing_symbol = (size_of_space_symbol - len(coin['symbol'])) * ' '
        print(coin['name'] + size_of_space_missing_coin +  coin['symbol'], size_of_space_missing_symbol, round(float(price),2))

def addToTextFile(stickerToAdd, amount, portfolio):
    print("Will add", stickerToAdd)
    print("Will add", amount)
    #portfolio[stickerToAdd]['price'] = float(amount) + float(portfolio[stickerToAdd]['price'])
    print(portfolio[stickerToAdd])
    with open('portfolio.txt', 'w') as out:
        for x in portfolio:
            out.write( x + ',')
        out.write('\n')
        for y in portfolio:
            if y == stickerToAdd:
                out.write(str(amount) +',')
            else:
                out.write(portfolio[y] +',')



parameters = parameters(1,199)
session = Session()
session.headers.update(HEADERS)
manager = portfolioManager()
response = manager.getCryptoData(session, LATESTURL, parameters)
guardian = True
while guardian:
    portfolio = getPortfolio()
    print("Here is your portfolio: ")
    print("Symbol: " + "Amount: " + "Market value: "  + "               Price: ")
    for y in portfolio:
        if y != '':
            price = response[y]['price']
            mv = price*float(portfolio[y])
            mv = str(round(mv,2))
            print(y + ':   ', portfolio[y], "     $: " + mv + '      $', round(response[y]['price'],2))
    printChoices()
    choice = int(input("Please insert choice: "))
    if choice == 1:
        top = topTen(response)
        input("Any button to go back ")
    if choice == 2:
        running = True
        while running:
            try: 
                stickerToAdd = input("Enter sticker you want to add: ")
                stickerToAdd = stickerToAdd.upper()
                portfolio[stickerToAdd]
                amount = float(input("Input amount (. to indicate decimal)"))
                addToTextFile(stickerToAdd,amount,portfolio)
                running = False
            except ValueError:
                print("Valid input please, a number ")
        input("Any button to go back ")

