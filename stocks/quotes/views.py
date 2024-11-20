from django.shortcuts import render
import requests
import json
import os

def home(request):
	api_request = requests.get(f"https://api.finazon.io/latest/finazon/us_stocks_essential/tickers?ticker=AAPL&apikey={os.getenv('API_KEY')}")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})