from flask import Flask, render_template, redirect, url_for
from src.dashboard import generate_dashboard


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
    return render_template(
        'dashboard.html',
        config=generate_dashboard(USER_ASSETS, CURRENCY)
    )


if __name__ == '__main__':
    app.run(debug=True)