import os
import sqlite3


def database_connection():
    if os.path.isfile('database.db') == True:
        return sqlite3.connect('database.db')
    else:
        connection = sqlite3.connect('database.db')
        with open('schema.sql') as f:
            connection.executescript(f.read())
        return connection


def insert_into_users(name, password):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO users (name, password) VALUES (?,?)',
        (name, password)
    )
    connection.commit()
    connection.close()


def get_all_users_data():
    connection = database_connection()
    users = connection.execute(
        'SELECT * FROM users'
    ).fetchall()
    connection.close()
    return users


def insert_into_assets(user_id, coin, amount, date):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO assets (user_id, coin, amount, date) VALUES (?,?,?,?)',
        (user_id, coin, amount, date)
    )
    connection.commit()
    connection.close()


def get_all_asset_data():
    connection = database_connection()
    assets = connection.execute(
        'SELECT * FROM assets'
    ).fetchall()
    connection.close()
    return assets