from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, time, csv

from endpoint_caller import EndpointCaller
from portfolio_manager import PortfolioManager
from printer import *
from file_service import *



LATESTURL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
HEADERS = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '85b403c5-f580-4b25-87dc-a88de76e0bf9',
}
CURRENCY = 'USD'



def parameters(start, limit):
    parameters = {
    # Where to start from in the list that the API wants to return
    'start':start,
    # Until what index of the list being returned
    'limit':limit,
    # I can always change this but it's easier to start with USD
    'convert':CURRENCY
    }
    return parameters


def load_param(param):
    pass

parameters = parameters(1,199)
session = Session()
session.headers.update(HEADERS)
print(session)
# Updating parameter for what we need
manager = PortfolioManager()
manager.params = parameters
response = manager.get_crypto_data(session, LATESTURL)
for y in response:
    print(y['symbol'])
guardian = True
while guardian:
    portfolio = get_portfolio()
    print_portfolio(portfolio, response)
    printChoices()
    choice = int(input("Please insert choice: "))
    if choice == 1:
        top = print_top_ten(response)
        input("Any button to go back ")
    elif choice == 2:
        running = True
        while running:
            try: 
                stickerToAdd = input("Enter ticker you want to add: ")
                stickerToAdd = stickerToAdd.upper()
                portfolio[stickerToAdd]
                amount = float(input("Input amount (. to indicate decimal)"))
                add_to_text_file(stickerToAdd,amount,portfolio)
                running = False
            except ValueError:
                print("Valid input please, a number ")
            input("Any button to go back ")

    
    # This option should clear your portfolio

        


        

