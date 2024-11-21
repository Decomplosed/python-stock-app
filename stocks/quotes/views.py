from django.shortcuts import render
import requests
import json
import os

def home(request):
	api_key = os.getenv('API_KEY')
	ticker_request = requests.get(f"https://api.finazon.io/latest/finazon/us_stocks_essential/tickers?ticker=AAPL&apikey={api_key}")
	ticker_price_request = requests.get(f"https://api.finazon.io/latest/finazon/us_stocks_essential/price?ticker=AAPL&apikey={api_key}")

	try:
		ticker_data = json.loads(ticker_request.content)
		ticker_price = json.loads(ticker_price_request.content)
		api = {
			"ticker_data": ticker_data,
			"ticker_price": ticker_price
		}
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})