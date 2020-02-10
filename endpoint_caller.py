from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class endpointCaller():
    def __init__(self):
        self.callerId = 1
    # The parameters into this method will have to be devised and sent from
    def getTop10(self, session, url,parameters):
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

