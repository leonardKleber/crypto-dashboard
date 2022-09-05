import datetime
from src.api import get_max_historical_data
from src.crypto import cut_historical_data
from src.chart import generate_chart


# Generates a configuration json for the dashboard page.
def generate_dashboard(user_assets, currency):
    all_coin_data = get_all_coin_data(user_assets, currency)
    if all_coin_data == 'connection error' or all_coin_data == 'rate limit reached':
        return all_coin_data
    else:
        summed_data = sum_up_historical_datas(user_assets, all_coin_data)
        performance = get_portfolio_performance(user_assets, all_coin_data)
        print(generate_user_assets(user_assets, all_coin_data))
        return {
            'chart': generate_user_charts(summed_data, performance),
            'performance': performance,
            'worth': get_portfolio_worth(summed_data),
            'assets': generate_user_assets(user_assets, all_coin_data)
        }


# Get current portfolio worth.
def get_portfolio_worth(portfolio_data):
    copy = portfolio_data.copy()
    copy.reverse()
    return copy[0]


# Convert date string from database to datetime object.
def date_to_datetime(date):
    day = date[0] + date[1]
    month = date[3] + date[4]
    year = date[6] + date[7] + date[8] + date[9]
    return datetime.date(int(year), int(month), int(day))


# Gets the number of days ago the user bought the asset.
def get_days_since_investment(date):
    today = datetime.date.today()
    difference = (today - date).days
    return difference


# Generates a configuration json for the different timeframe charts.
def generate_user_charts(portfolio_data, performance):
    return {
        'week': generate_chart(cut_historical_data(portfolio_data, 7), performance),
        'month': generate_chart(cut_historical_data(portfolio_data, 30), performance),
        'year': generate_chart(cut_historical_data(portfolio_data, 365), performance),
        'three_years': generate_chart(cut_historical_data(portfolio_data, 1095), performance),
        'five_years': generate_chart(cut_historical_data(portfolio_data, 1825), performance),
        'total': generate_chart(portfolio_data, performance)
    }


# Generates a configuration json to list all user assets.
def generate_user_assets(user_assets, all_coin_data):
    all_historical_data = total_historical_data(user_assets, all_coin_data)
    assets = []
    counter = 0
    for i in user_assets:
        asset_list = all_historical_data[counter]
        cost = asset_list[0]
        reverse_asset_list = list(reversed(asset_list))
        worth = reverse_asset_list[0]
        gain = get_asset_performance(cost, worth)
        assets.append({
            'coin': i['coin'],
            'amount': i['amount'],
            'cost': cost,
            'worth': worth,
            'gain': gain
        })
        counter = counter + 1
    return assets


# Gets a list of different coins the user owns and its historical data.
def get_all_coin_data(user_assets, currency):
    coins = []
    for i in user_assets:
        if i['coin'] not in coins:
            coins.append(i['coin'])
    data = []
    for i in coins:
        api_response = get_max_historical_data(i, currency)
        if api_response == 'connection error' or api_response == 'rate limit reached':
            return api_response
        else:
            data.append({'coin': i, 'data': api_response})
    return data


# Generates the total data since buy of each coin in the portfolio.
def total_historical_data(user_assets, all_coin_data):
    data = []
    for i in user_assets:
        days = get_days_since_investment(date_to_datetime(i['date']))
        coin_data = []
        for j in all_coin_data:
            if i['coin'] == j['coin']:
                coin_data = j['data']
        weighted_data = cut_historical_data(coin_data, days)
        for j in range(len(weighted_data)):
            weighted_data[j] = round(weighted_data[j] * i['amount'], 2)
        data.append(weighted_data)
    return data


# Sums up all relative historical data since buy of single coins in the users portfolio.
def sum_up_historical_datas(user_assets, all_coin_data):
    all_historical_data = total_historical_data(user_assets, all_coin_data)
    max_len = 0
    for i in all_historical_data:
        if len(i) > max_len:
            max_len = len(i)
    equal_length_data = []
    for i in all_historical_data:
        equal_length_data.append(cut_historical_data(i, max_len))
    data = []
    for i in range(max_len):
        summed = 0
        for j in range(len(equal_length_data)):
            summed = summed + equal_length_data[j][i]
        data.append(round(summed, 2))
    return data


# Gets the overall performance of the user portfolio.
def get_portfolio_performance(user_assets, all_coin_data):
    all_historical_data = total_historical_data(user_assets, all_coin_data)
    performances = []
    for i in all_historical_data:
        investment = i[0]
        i.reverse()
        current_value = i[0]
        gain = ((current_value - investment) / investment) * 100
        performances.append(round(gain, 2))
    sum_performances = 0
    for i in performances:
        sum_performances = sum_performances + i
    return round(sum_performances / len(performances), 2)


# Gets the performance of a single asset.
def get_asset_performance(investment, current_value):
    return round((((current_value - investment) / investment) * 100), 2)