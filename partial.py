from functools import partial
import datetime as dt
import pandas_datareader as web

def get_stock_data(ticker, start, end):
  return web.DataReader(ticker, "yahoo", start, end)

print(get_stock_data("AAPL"), "1/1/2018", "1/1/2019")

# Same result as previous call
get_aapl_data = partial(get_stock_data, "AAPL")
get_tsla_data = partial(get_stock_data, "TSLA")
get_googl_data = partial(get_stock_data, "GOOGL")

print(get_aapl_data("1/1/2018", "1/1/2019"))
print(get_tsla_data("1/1/2018", "1/1/2019"))
print(get_googl_data("1/1/2018", "1/1/2019"))

# Reusing previous func but hardcoding start and defining end
get_stock_data_from2018 = partial(get_stock_data, start="1/1/2018")
print(get_stock_data_from2018("META", end="1/1/2019"))

# Reusing previous func but hardcoding start and end
get_stock_data_from2018_to_2020 = partial(get_stock_data, start="1/1/2018", end="1/1/2020")
print(get_stock_data_from2018_to_2020("GS"))
