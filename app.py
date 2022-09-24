from auth import *
from src.api import get_all_available_coins
from db import get_all_asset_data, insert_into_assets
from flask import Flask, session, render_template, request, redirect, url_for
from src.dashboard import generate_dashboard, check_valid_date, get_number_of_coins


app = Flask(__name__)
app.secret_key = 'secret_key'


def get_user_assets(user_id):
    all_asset_data = get_all_asset_data()
    user_assets = []
    for i in all_asset_data:
        if i[1] == user_id:
            user_assets.append({
                'id': i[0],
                'user_id': i[1],
                'coin': i[2],
                'amount': i[3],
                'date': i[4]
            })
    return user_assets


@app.route('/')
def index():
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    if 'id' in session:
        if session['id'] == None:
            return redirect(url_for('login'))
        else:
            user_assets = get_user_assets(session['id'])
            if len(user_assets) == 0:
                return render_template('init.html')
            else:
                config = generate_dashboard(user_assets, 'usd')
                if config == 'connection error':
                    return render_template('connection_error.html')
                elif config == 'rate limit reached':
                    return render_template('rate_limit.html')
                else:
                    return render_template(
                        'dashboard.html',
                        config=config
                    )
    else:
        return redirect(url_for('login'))


@app.route('/add_asset', methods=['GET', 'POST'])
def add_asset():
    if 'id' in session:
        if session['id'] == None:
            return redirect(url_for('login'))
        else:
            user_assets = get_user_assets(session['id'])
            if get_number_of_coins(user_assets) == 40:
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
                        insert_into_assets(session['id'], coin, float(amount), date)
                        #USER_ASSETS.append({
                        #    'id': 'x',
                        #    'user_id': 1,
                        #    'coin': coin,
                        #    'amount': float(amount),
                        #    'date': date
                        #})
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
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if check_login_validity(name, password) == True:
            session['id'] = get_user_id(name)
            return redirect(url_for('index'))
        else:
            return render_template(
                'login.html',
                username_message='Unvalid username.',
                password_message='Unvalid password.'
            )
    else:
        return render_template(
            'login.html',
            username_message='',
            password_message=''
        )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if check_name_availability(name) == True:
            create_user(name, password)
            return redirect(url_for('login'))
        else:
            return render_template(
                'register.html',
                username_message='This username is not available.',
                password_message=''
            )
    else:
        return render_template(
            'register.html',
            username_message='',
            password_message=''
        )


@app.route('/logout')
def logout():
    session['id'] = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)