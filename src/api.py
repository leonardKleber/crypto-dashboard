import requests


# Handles all API calls and checks for connection and URL errors.
def get_api_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json
    elif response.status_code == 429:
        return 'rate limit reached'
    else:
        return 'connection error'


# Obtains a coin's historical data up to the earliest possible point.
def get_max_historical_data(coin, currency):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency={currency}&days=max'
    response = get_api_response(url)
    if response == 'rate limit reached' or response == 'connection error':
        return response
    else:
        prices = []
        for i in response['prices']:
            price = round(i[1], 2)
            prices.append(price)
        return prices


# Obtains a list of all coins that are supported by the CoinGecko API.
def get_all_available_coins():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    response = get_api_response(url)
    if response == 'rate limit reached' or response == 'connection error':
        return response
    else:
        coins = []
        for i in response:
            coins.append(i['id'])
        return coins