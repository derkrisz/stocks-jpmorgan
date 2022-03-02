import datetime

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