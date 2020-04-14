from endpoint_caller import EndpointCaller

class PortfolioManager():
    def __init__(self):
        self.params = {}
        self.callerId = 1
        self.top10Data = {}
        # An object that we get from the API to contact it again
        self.session = {}

    def update_parameters(self, params):
        self.params = params

    # The parameters into this method will have to be devised and sent from elsewhere
    def get_crypto_data(self, session, url):
        endpointCall = EndpointCaller()
        top10List = endpointCall.getTop10(session, url, self.params)
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