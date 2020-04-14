def printChoices():
    print("What would you like to do? ")
    print("1. View top 10")
    print("2. Add to holding")

def print_portfolio(portfolio, response):
    print("Here is your portfolio: ")
    print("Symbol: " + "Amount: " + "Market value: "  + "               Price: ")
    for y in portfolio:
            if y != '':
                price = response[y]['price']
                mv = price*float(portfolio[y])
                mv = str(round(mv,2))
                print(y + ':   ', portfolio[y], "     $: " + mv + '      $', round(response[y]['price'],2))


def print_top_ten(response):
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
