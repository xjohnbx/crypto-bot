# This is a file that contains all the network calls for coinbaseAPI

from coinbaseAPIAuth import CoinbaseAPIAuth
import json, requests
from pprint import pprint

class CoinbaseAPIRoutes():
	def __init__(self):
		self.auth = CoinbaseAPIAuth()
		self.api_url = 'https://api.pro.coinbase.com/'
		
	def getAccount(self):
		getRequest = requests.get(self.api_url + 'accounts', auth=self.auth)

