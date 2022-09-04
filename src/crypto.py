from api import get_api_response, get_max_historical_data


def get_current_price(historical_data):
    data = historical_data
    data.reverse()
    return data[0]


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
        new_data = historical_data.copy()
        difference = days - len(new_data)
        new_data.reverse()
        for i in range(difference):
            new_data.append(0)
        new_data.reverse()
        return new_data
    else:
        return historical_data