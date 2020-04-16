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

def get_symbol(response):
    symbols = []
    for y in response:
        if y != '':
            symbol = response[y]['symbol']
            symbols.append(symbol)
    return symbols

def run_program(symbols, response):
    guardian = True
    while guardian:
        portfolio = get_portfolio(symbols)
        print_portfolio(portfolio, response)
        printChoices()
        choice = input("Please insert choice: ")
        if choice == '1':
            top = print_top_ten(response)
            input("Any button to go back ")
        elif choice == '2':
            running = True
            while running:
                try: 
                    ticker_to_add = input("Enter ticker you want to change: ")
                    ticker = ticker_to_add.upper()
                    portfolio[ticker]
                    amount = float(input("Input amount (. to indicate decimal)"))
                    add_to_text_file(ticker,amount,portfolio)
                    running = False
                except ValueError:
                    print("Valid input please, a number ")
                input("Any button to go back ")
        elif choice == '9':
            reset_portfolio(symbols)
            

parameters = parameters(1,199)
session = Session()
session.headers.update(HEADERS)
print(session)
# Updating parameter for what we need
manager = PortfolioManager()
manager.params = parameters
response = manager.get_crypto_data(session, LATESTURL)
symbols = get_symbol(response)
run_program(symbols, response)


            


            

