import matplotlib.pyplot as plt
import matplotlib.dates as mdates

"""
    Input: queried data, start_date, end_date.
    Output: None.
    Does: Plots the dates on the x-axis and closing prices on the y-axis.
"""
def visualize(data, start, end, symbol):
    dates = data.get('date')
    close_prices = data.get('close')

    # Plots the dates and closing prices
    fig, ax = plt.subplots(figsize = (8,8))
    plt.suptitle("Closing prices for " + symbol.upper())
    plt.ylabel("Closing prices ($)")
    plt.xlabel("Date (Month/Day/Year)")
    plt.plot(dates, close_prices)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.xticks(rotation=45)
    plt.show()
