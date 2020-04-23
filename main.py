from web_functions import query_data
from visualize_functions import visualize

def user_input_date(str_x):
    print("Enter a " + str_x + " year: ")
    year = int(input())

    print("Enter a " + str_x + " month: ")
    month = int(input())

    print("Enter a " + str_x + " day: ")
    day = int(input())

    date = str(year) + "-" + str(month) + "-" + str(day)
    return date

def main():
    print("Stock History Grapher")
    print("---------------------")

    # Company stock symbol
    print("Enter a company stock symbol: ")
    symbol = input()

    # Start date the user enters
    start_date = user_input_date("start")

    # End date the user enters
    end_date = user_input_date("end")

    # Data contains all the stock values for each day between both dates
    data = query_data(symbol, start_date, end_date)

    # Graphs the data as a line graph
    visualize(data, start_date, end_date, symbol)

main()
