# StockHistoryGrapher

Required packages:
1) quandl and all its dependancies.
    pip install quandl
2) matplotlib.pyplot
    pip install matplotlib
3) matplotlib.dates

About:
A stock grapher that uses Quandl API to obtain stock values for various companies.
Users can enter a company's stock symbol and the time frame for the stock prices they want to see.
The program filters the dataframe and only gets the 'ticker', 'date', and 'close' columns from the table that Quandl provides.
Implements matplotlib to plot the stock values over a specific period of time.

How to run:
1) Run file main.py
2) Respond to the text prompts via keyboard inputs.
