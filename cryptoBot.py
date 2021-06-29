# This is a python progarm that interacts with the Coinbase Pro APIs

from coinbaseAPIRoutes import CoinbaseAPIRoutes
from currencyEnum import Currency

def main():
	provider = CoinbaseAPIRoutes()
#	provider.getAccountWithId(Currency.ONEINCH)
	provider.getAccounts()
#	provider.getAccountHistory()
	
main()

 
