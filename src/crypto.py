# Gets the current price of a coin from its historical data.
def get_current_price(historical_data):
    data = historical_data.copy()
    data.reverse()
    return data[0]


# Gets the price that a coin had a number of days ago from its historical data.
def get_price_days_ago(historical_data, days_ago):
    data = historical_data.copy()
    data.reverse()
    for i in range(len(data)):
        if i == days_ago:
            return data[i]
    return 0


# Gets the performance of an investment based on the time of the investment.
# def get_performance(historical_data, investment_days_ago):
#     investment = get_price_days_ago(historical_data, investment_days_ago)
#     current_price = get_current_price(historical_data)
#     gain = ((current_price - investment) / investment) * 100
#     return round(gain, 2)


# Gets the historical data of a coin from today to a number of days back.
def cut_historical_data(historical_data, days):
    if len(historical_data) > days:
        new_data = []
        data = historical_data.copy()
        data.reverse()
        for i in range(days):
            new_data.append(data[i])
        new_data.reverse()
        return new_data
    elif len(historical_data) < days:
        data = historical_data.copy()
        difference = days - len(data)
        data.reverse()
        for i in range(difference):
            data.append(0)
        data.reverse()
        return data
    else:
        return historical_data