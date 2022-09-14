# Crypto Portfolio Dashboard
A dashboard for the cryptocurrency portfolio tracking tool and analyzer **My Virtual Wallet** built with Flask, CoinGecko API and Chart.js. 

This project is part of a a remastered version of my final project for HarvardX's CS50 online course. You can find a short presentation of the old project here:
```
https://www.youtube.com/watch?v=k6B14KtYqks
```

# Limitations
This project uses the CoinGecko API to gather real-time information and historical data on a wide range of crypto currencies. The API comes with a free tier that allows up to 50 API calls a minute. Because of the limited number of calls, this app focuses on the historical data of each coin for charting and analysis purposes. Unfortunately, the last entry of the historical data is the data of the day prior. That means that the app always lags one day behind the current course to minimize the number of calls that must be made to gather all the data.

Because of the call limitation, the number of different coins per portfolio is also limited to 40 coins.

## Set up the project
### 1. Clone the project
Clone the project to your machine. Make sure Python3 and pip are already installed on your system.
### 2. Install requirements
Install all requirements with the following command:
```
pip3 install -r requirements.txt
```
### 3. Run the app
Run the app like the following:
```
python3 app.py
```
