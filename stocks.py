import datetime
from statistics import geometric_mean

class StocksList:
    def __init__(self):
        self.stocks = []

    @property
    def stocks(self):
        return self._stocks

    @stocks.setter
    def stocks(self, stocks):
        self._stocks = stocks

    def add_stock(self, stock):
        self.stocks.append(stock)

    def calculate_gcb_all_share_index(self):
        volume_weighted_stock_prices = []
        for stock in self.stocks:
            volume_weighted_stock_price = stock.calculate_volume_weighted_stock_price()
            volume_weighted_stock_prices.append(volume_weighted_stock_price)
        return round(geometric_mean(volume_weighted_stock_prices), 3)



class Stock:
    def __init__(self, symbol, type, last_dividend=0, fixed_dividend=None, par_value=100):
        self._symbol = symbol
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.trades = []

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        allowed_types = ['Common', 'Preferred']
        if type not in allowed_types:
            raise ValueError('Type must be either Common or Preferred')
        self._type = type

    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, last_dividend):
        self._last_dividend = last_dividend

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, fixed_dividend):
        self._fixed_dividend = fixed_dividend

    @property
    def par_value(self):
        return self._par_value

    @par_value.setter
    def par_value(self, par_value):
        self._par_value= par_value

    @property
    def trades(self):
        return self._trades

    @trades.setter
    def trades(self, trades):
        self._trades = trades


    def calculate_dividend_yield(self, price):
        if self.type == 'Common':
            return round(self.last_dividend / price, 3)
        else:
            return round((self.fixed_dividend / 100 * self.par_value) / price, 3)

    def calculate_pe_ratio(self, price):
        return round(price / self.last_dividend, 3)

    def record_trade(self, quantity, indicator, price, timestamp=datetime.datetime.now()):
        if indicator not in ['Buy', 'Sell']:
            raise ValueError('Indicator must be set to "Buy" or "Sell"')
        trade = {'quantity': quantity, 'indicator': indicator, 'price': price, 'timestamp': timestamp}
        self.trades.append(trade)

    def calculate_volume_weighted_stock_price(self):
        now, five_minutes_ago = datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(minutes=5)
        sum_of_traded_price_and_quantity = sum_of_quantity = 0
        for trade in self.trades:
            if five_minutes_ago < trade['timestamp'] < now:
                sum_of_traded_price_and_quantity += trade['price'] * trade['quantity']
                sum_of_quantity += trade['quantity']
        return round(sum_of_traded_price_and_quantity / sum_of_quantity, 3)




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