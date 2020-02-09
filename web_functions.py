import quandl

QUANDL_API_KEY = "8a2vLQ2Dzi6Q8F5QCtzA"
QUANDL_SRC = "WIKI/PRICES"
quandl.ApiConfig.api_key = QUANDL_API_KEY

"""
    Input: String (stock symbol/ticker), String (date), String (date).
    Output: Hashtable (ticker/date/close)
    Does: Calls Quandl API and gets the closing prices for the given ticker
        for a specified time frame.
"""
def query_data(symbol, start, end):
    data = quandl.get_table(QUANDL_SRC,
                            qopts={'columns': ['ticker', 'date', 'close']},
                            ticker=[symbol],
                            date={'gte':start, 'lte':end})
    return data
