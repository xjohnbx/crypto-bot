# This is a python progarm that interacts with the Coinbase Pro APIs

from coinbaseAPIRoutes import CoinbaseAPIRoutes
from currencyEnum import Currency

def main():
	provider = CoinbaseAPIRoutes()

# Working Routes:

	# Account Routes:
	#	provider.getAllAccounts()
	#	provider.getAccountWithId(Currency.ATOM)
	#	provider.getAccountHistory(Currency.ATOM)
	#	provider.getAccountHolds(Currency.ATOM)

	# Order Routes
	#	provider.placeOrder(price='.01', product_id='DOGE-USD', side='buy', size='1')


# Routes that are being worked on:



	
main()

 
