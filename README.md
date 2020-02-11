# StockHistoryGrapher

Required packages:
1) quandl (pip install quandl)
2) matplotlib (pip install matplotlib)
    

About:
A stock grapher that uses Quandl API to obtain stock values for various companies.
Users can enter a company's stock symbol and the time frame for the stock prices they want to see.
The program filters the dataframe and only gets the 'ticker', 'date', and 'close' columns from the table that Quandl provides.
Implements matplotlib to plot the stock values over a specific period of time.

How to run:
1) Run file main.py
2) Respond to the text prompts via keyboard inputs.
    Example:
    - Apple's stock symbol: AAPL
    - Start year: 2017
    - Start month: 3
    - Start day: 18
    - End year: 2018
    - End month: 1
    - End day: 20
