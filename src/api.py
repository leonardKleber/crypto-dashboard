import requests


def get_api_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        return json
    elif response.status_code == 429:
        return 'rate limit reached'
    else:
        return 'connection error'


def get_max_historical_data(coin, currency):
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency={currency}&days=max'
    response = get_api_response(url)
    if response == 'rate limit reached':
        return response
    elif response == 'rate limit reached':
        return response
    else:
        prices = []
        for i in response['prices']:
            price = round(i[1], 2)
            prices.append(price)
        return prices