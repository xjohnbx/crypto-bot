# Python file to hold variables from .env

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
API_PASSWORD = os.getenv('API_PASSWORD')
