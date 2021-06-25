# This is a file that sets the headers and authorizes our API calls

import envSettings
import json, hmac, hashlib, time, requests, base64
from pprint import pprint

class CoinbaseAPIAuth():
	def __init__ (self):
		self.api_key = envSettings.API_KEY
		self.api_secret = envSettings.API_SECRET
		self.passphrase = envSettings.API_PASSWORD
		
	def __call__(self, request):
		timestamp = str(time.time())
		message = timestamp + request.method + request.path_url + (request.body or '')
		hmac_key = base64.b64decode(self.api_secret)
		signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
		signature_b64 = base64.b64encode(signature.digest())

		request.headers.update({
			'CB-ACCESS-SIGN': signature_b64,
			'CB-ACCESS-TIMESTAMP': timestamp,
			'CB-ACCESS-KEY': self.api_key,
			'CB-ACCESS-PASSPHRASE': self.passphrase,
			'Content-Type': 'application/json'
		})
		
		return request
