import csv

def get_portfolio():
    with open('portfolio.csv') as csv_file:
        csvReader = csv.DictReader(csv_file, delimiter = ';')
        csv_reader = csv_file.readlines()
        symbolList = csv_reader[0].split(',')
        priceList = csv_reader[1].split(',')
        portfolio = {}
        for x,y in zip(symbolList, priceList):
            if x != '':
                portfolio[x.strip('\n')] =y
        print("Returning portfolio ", portfolio)
        return portfolio

def add_to_text_file(stickerToAdd, amount, portfolio):
    print("Will add", stickerToAdd)
    print("Will add", amount)
    #portfolio[stickerToAdd]['price'] = float(amount) + float(portfolio[stickerToAdd]['price'])
    print(portfolio[stickerToAdd])
    with open('portfolio.csv', 'w') as out:
        for x in portfolio:
            out.write( x + ',')
        out.write('\n')
        for y in portfolio:
            if y == stickerToAdd:
                out.write(str(amount) +',')
            else:
                out.write(portfolio[y] +',')