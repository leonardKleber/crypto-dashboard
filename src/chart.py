import random


# Generates a configuration json for the chart on dashboard page.
def generate_chart(data, performance):
    if performance > 0:
        color_string = 'rgb(32,192,32)'
    else:
        color_string = 'rgb(255,0,0)'
    config = {
        'type': 'line',
        'data': {
            'labels': data,
            'datasets': [{
                'backgroundColor': color_string,
                'borderColor': color_string,
                'data': data
            }]
        },
        'options': {
            'scales': {
                'xAxis': {
                    'display': False
                },
                'yAxis': {
                    'display': False
                }
            },
            'elements': {
                'point': {
                    'radius': 0
                }
            },
            'plugins': {
                'legend': {
                    'display': False
                }
            }
        }
    }
    return config


# Generates a configuration json for a doughnut chart that showes the portfolios allocation.
def generate_doughnut_chart(user_assets, all_coin_data):
    coin_names = []
    coin_amounts = []
    for i in user_assets:
        if i['coin'] in coin_names:
            index = coin_names.index(i['coin'])
            coin_amounts[index] = coin_amounts[index] + i['amount']
        else:
            coin_names.append(i['coin'])
            coin_amounts.append(i['amount'])
    coin_worths = []
    counter = 0
    for i in all_coin_data:
        price = list(reversed(i['data']))[0]
        worth = price * coin_amounts[counter]
        coin_worths.append(worth)
        counter = counter + 1
    total_worth = 0
    for i in coin_worths:
        total_worth = total_worth + i
    config = {
        'type': 'doughnut',
        'data': {
            'labels': coin_names,
            'datasets': [{
                'data': coin_worths,
                'backgroundColor': generate_colors(coin_names),
            }]
        }
    }
    return config


# Generates a random color for each coin.
def generate_colors(coin_names):
    color_list = []
    color_values = [
        'rgb(32,32,32)',
        'rgb(64,64,64)',
        'rgb(96,96,96)',
        'rgb(128,128,128)',
        'rgb(160,160,160)',
        'rgb(192,192,192)',
        'rgb(244,244,244)'
    ]
    for i in coin_names:
        color_list.append(color_values[random.randint(0, len(color_values)-1)])
    return color_list