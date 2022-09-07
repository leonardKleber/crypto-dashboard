from flask import Flask, render_template, redirect, url_for, request
from src.dashboard import generate_dashboard
from src.add_asset import get_all_available_coins


# A pseudo database for testing purposes.
USER_ASSETS = [
    {'id': 1, 'user_id': 1, 'coin': 'bitcoin', 'amount': 1, 'date': '01-01-2021'},
    {'id': 2, 'user_id': 1, 'coin': 'cardano', 'amount': 100, 'date': '30-07-2021'},
    {'id': 3, 'user_id': 1, 'coin': 'ethereum', 'amount': 1, 'date': '01-01-2021'},
    {'id': 4, 'user_id': 1, 'coin': 'bitcoin', 'amount': 1, 'date': '01-12-2020'},
    {'id': 5, 'user_id': 1, 'coin': 'bitcoin', 'amount': 5, 'date': '01-01-2022'}
]

# Default currency of the application.
CURRENCY = 'usd'


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
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
    if request.method == 'POST':
        coin = request.form.get('coin')
        amount = request.form.get('amount')
        date = request.form.get('date')
        USER_ASSETS.append({
            'id': 'x',
            'user_id': 1,
            'coin': coin,
            'amount': int(amount),
            'date': date
        })
        return redirect(url_for('dashboard'))
    else:
        supported_coins = get_all_available_coins()
        if supported_coins == 'connection error':
            return render_template('connection_error.html')
        elif supported_coins == 'rate limit reached':
            return render_template('rate_limit.html')
        else:
            return render_template(
                'add_asset.html',
                coins=supported_coins
            )


if __name__ == '__main__':
    app.run(debug=True)