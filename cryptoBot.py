# This is a python progarm that interacts with the Coinbase Pro APIs

from coinbaseAPIRoutes import CoinbaseAPIRoutes

def main():
	provider = CoinbaseAPIRoutes()
	provider.getAccount()
	
main()

 
