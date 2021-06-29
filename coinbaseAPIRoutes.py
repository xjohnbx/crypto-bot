# This is a file that contains all the network calls for coinbaseAPI

from coinbaseAPIAuth import CoinbaseAPIAuth
import json, requests
from currencyEnum import Currency

from pprint import pprint

class CoinbaseAPIRoutes():
	def __init__(self):
		self.auth = CoinbaseAPIAuth()
		self.api_url = 'https://api.pro.coinbase.com/'
		
	def getAccounts(self):
		getRequest = requests.get(self.api_url + 'accounts', auth=self.auth)
		pprint(getRequest.json())

	def getAccountWithId(self, id):
		getRequest = requests.get(self.api_url +'accounts/' + id.value, auth=self.auth)
		pprint(getRequest.json())
		
	def getAccountHistory(self, ):
		getRequest = requests.get(self.api_url + 'accounts/ledger', auth=self.auth)
		pprint(getRequest.json())
		
		
#	def getPriceData(self):
#
# Our next step is going to be placing an order.
# This is a real order so don't do anything ridiculous
# Steps:
# 		- Create getOrder(self, product):
# 		- Create Enum for products on Coinbase to send in the 'product' paramater
