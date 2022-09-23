from auth import *
from db import get_all_asset_data, insert_into_assets
from flask import Flask, session, render_template, request, redirect, url_for


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
            return 'This is the Dashboard'
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