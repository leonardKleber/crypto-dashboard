from flask import Flask, render_template, redirect, url_for, request
from src.dashboard import generate_dashboard, check_valid_date
from src.api import get_all_available_coins


# A pseudo database for testing purposes.
USER_ASSETS = [
#    {'id': 1, 'user_id': 1, 'coin': 'bitcoin', 'amount': 1.0, 'date': '01-01-2021'},
#    {'id': 2, 'user_id': 1, 'coin': 'cardano', 'amount': 100000.0, 'date': '30-07-2021'},
#    {'id': 3, 'user_id': 1, 'coin': 'ethereum', 'amount': 100.0, 'date': '01-01-2021'},
#    {'id': 4, 'user_id': 1, 'coin': 'bitcoin', 'amount': 5.0, 'date': '01-12-2020'},
#    {'id': 5, 'user_id': 1, 'coin': 'bitcoin', 'amount': 5.0, 'date': '01-01-2022'}
]

# Default currency of the application.
CURRENCY = 'usd'


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    if len(USER_ASSETS) == 0:
        return render_template('init.html')
    else:
        config = generate_dashboard(USER_ASSETS, CURRENCY)
        if config == 'connection error':
            return render_template('connection_error.html')
        elif config == 'rate limit reached':
            return render_template('rate_limit.html')
        else:
            return render_template(
                'dashboard.html',
                config=config
            )


@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if len(USER_ASSETS) == 40:
        return redirect(url_for('dashboard'))
    else:
        supported_coins = get_all_available_coins()
        if request.method == 'POST':
            coin = request.form.get('coin')
            amount = request.form.get('amount')
            date = request.form.get('date')

            error_count = 0
            if coin in supported_coins:
                coin_message = ''
            else:
                coin_message = 'The coin you entered is not supported by the CoinGecko API.'
                error_count = error_count + 1
            amount_message = ''
            if check_valid_date(date) == False:
                date_message = 'The date you entered is unvalid. Please stick to the format: dd-mm-yyyy'
                error_count = error_count + 1
            else:
                date_message = ''
            if error_count > 0:
                return render_template(
                    'add_asset.html',
                    coins=supported_coins,
                    messages={
                        'coin': coin_message,
                        'amount': amount_message,
                        'date': date_message
                    }
                )
            else:
                USER_ASSETS.append({
                    'id': 'x',
                    'user_id': 1,
                    'coin': coin,
                    'amount': float(amount),
                    'date': date
                })
                return redirect(url_for('dashboard'))
        else:
            if supported_coins == 'connection error':
                return render_template('connection_error.html')
            elif supported_coins == 'rate limit reached':
                return render_template('rate_limit.html')
            else:
                return render_template(
                    'add_asset.html',
                    coins=supported_coins,
                    messages={
                        'coin': '',
                        'amount': '',
                        'date': ''
                    }
                )


if __name__ == '__main__':
    app.run(debug=True)
