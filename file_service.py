import csv

def get_portfolio(symbols = 'adsfs'):
    new_dict = {}
    with open('portfolio.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',')
        #csv_reader = csv_file.readlines()
        for keys in csv_reader:
            for key in keys:
                #print(keys[key])
                new_dict[key] = keys[key]
        return new_dict

def add_to_text_file(stickerToAdd, amount, portfolio):
    print("Will add", stickerToAdd)
    print("Will add", amount)
    #portfolio[stickerToAdd]['price'] = float(amount) + float(portfolio[stickerToAdd]['price'])
    print(portfolio[stickerToAdd])
    
    with open('portfolio.csv', 'w') as out:
        symbols = []
        for x in portfolio:
            symbols.append(x)
        fieldnames = symbols
        writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter = ',')
        writer.writeheader()
        

def reset_portfolio(symbols):
    with open('portfolio.csv', 'w') as f_out:
        #csvReader = csv.DictReader(f_in, delimiter = ';')
        fieldnames = symbols
        new_dict = {}
        writer = csv.DictWriter(f_out, fieldnames=fieldnames, delimiter = ',')
        writer.writeheader()
        for y in symbols:
            new_dict[y] = 'emp'
        writer.writerow(new_dict)
    
