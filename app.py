from flask import Flask, render_template, redirect, url_for


# A pseudo database for testing purposes.
DB = [
    {'id': 1, 'user_id': 1, 'coin': 'bitcoin', 'amount': 1, 'date': '01-01-2020'},
    {'id': 2, 'user_id': 1, 'coin': 'cardano', 'amount': 100, 'date': '30-07-2021'},
    {'id': 3, 'user_id': 1, 'coin': 'ethereum', 'amount': 1, 'date': '01-01-2021'},
    {'id': 4, 'user_id': 1, 'coin': 'bitcoin', 'amount': 1, 'date': '01-12-2020'}
]

# Default currency of the application.
CURRENCY = 'usd'


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)