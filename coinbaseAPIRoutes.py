# This is a file that contains all the network calls for coinbaseAPI

from coinbaseAPIAuth import CoinbaseAPIAuth
import json, requests
from currencyEnum import Currency

from pprint import pprint

class CoinbaseAPIRoutes():
	def __init__(self):
		self.auth = CoinbaseAPIAuth()
		self.api_url = 'https://api.pro.coinbase.com/'
		
		
	# Account Routes
	def getAllAccounts(self):
		getRequest = requests.get(self.api_url + 'accounts', auth=self.auth)
		pprint(getRequest.json())

	def getAccountWithId(self, id):
		getRequest = requests.get(self.api_url +'accounts/' + id.value, auth=self.auth)
		pprint(getRequest.json())
		
	def getAccountHistory(self, id):
		getRequest = requests.get(self.api_url + 'accounts/' + id.value + '/ledger', auth=self.auth)
		pprint(getRequest.json())
	
	def getAccountHolds(self, id):
		getRequest = requests.get(self.api_url + 'accounts/' + id.value + '/holds', auth=self.auth)
		pprint(getRequest.json())
		
	
	# Order Routes
	def placeOrder(self, price, product_id, side, size):
		postRequest = requests.post(self.api_url + 'orders', data=json.dumps({'size': size, 'price': price, 'side': side, 'product_id': product_id}), auth=self.auth)
		pprint(postRequest.json())
