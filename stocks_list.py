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