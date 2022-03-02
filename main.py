import datetime
from stock import Stock
from stocks_list import StocksList

if __name__ == '__main__':

    someStock = Stock('POP', 'Common', 8)
    otherStock = Stock('GIN', 'Preferred', 8, 2, 100)
    print(someStock.calculate_dividend_yield(10))
    print(otherStock.calculate_dividend_yield(4))
    print(someStock.calculate_pe_ratio(10))
    print(otherStock.calculate_pe_ratio(4))
    someStock.record_trade(10, 'Buy', 5)
    someStock.record_trade(6, 'Sell', 3)
    otherStock.record_trade(5, 'Buy', 2)
    otherStock.record_trade(4, 'Sell', 4)
    ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
    otherStock.record_trade(10, 'Buy', 3, ten_minutes_ago)
    print(someStock.calculate_volume_weighted_stock_price())
    stock_list = StocksList()
    stock_list.add_stock(otherStock)
    stock_list.add_stock(someStock)
    print(stock_list.calculate_gcb_all_share_index())