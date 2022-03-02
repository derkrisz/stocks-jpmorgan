import datetime, unittest
from stocks import Stock, StocksList

class testStock(unittest.TestCase):

    def setUp(self):
        self.stock_one = Stock('POP', 'Common', 8)
        self.stock_two = Stock('GIN', 'Preferred', 8, 2, 100)
        self.stock_one.record_trade(10, 'Buy', 5)
        self.stock_one.record_trade(6, 'Sell', 3)
        self.stock_two.record_trade(5, 'Buy', 2)
        self.stock_two.record_trade(4, 'Sell', 4)
        self.stock_list = StocksList()
        self.stock_list.add_stock(self.stock_one)
        self.stock_list.add_stock(self.stock_two)

    def test_stock_type_exception(self):
        with self.assertRaises(ValueError) as e:
            result = Stock('GIN', 'Mutual', 3)
        self.assertEqual(str(e.exception), 'Type must be either Common or Preferred')
    
    def test_record_trade_exception(self):
        with self.assertRaises(ValueError) as e:
            result = self.stock_one.record_trade(1, 'Hold', 2)
        self.assertEqual(str(e.exception), 'Indicator must be set to "Buy" or "Sell"')
    
    def test_calculate_dividend_yield(self):
        stock_one_dividend_yield = self.stock_one.calculate_dividend_yield(10)
        stock_two_dividend_yield = self.stock_two.calculate_dividend_yield(4)
        self.assertEqual(stock_one_dividend_yield, 0.8)
        self.assertEqual(stock_two_dividend_yield, 0.5)

    def test_calculate_pe_ratio(self):
        stock_one_pe_ratio = self.stock_one.calculate_pe_ratio(15)
        stock_two_pe_ratio= self.stock_two.calculate_pe_ratio(9)
        self.assertEqual(stock_one_pe_ratio, 1.875)
        self.assertEqual(stock_two_pe_ratio, 1.125)

    def test_calculate_volume_weighted_stock_price(self):
        stock_one_volume_weighted_stock_price = self.stock_one.calculate_volume_weighted_stock_price()
        self.assertEqual(stock_one_volume_weighted_stock_price, 4.25)

    def test_calculate_volume_weighted_stock_price_only_last_five_minutes(self):
        ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
        self.stock_two.record_trade(9, 'Sell', 6, ten_minutes_ago)
        stock_two_volume_weighted_stock_price = self.stock_two.calculate_volume_weighted_stock_price()
        self.assertNotEqual(stock_two_volume_weighted_stock_price, 4.44)
        self.assertEqual(stock_two_volume_weighted_stock_price, 2.889)

    def test_calculate_gcb_all_share_index(self):
        gcb_all_share_index = self.stock_list.calculate_gcb_all_share_index()
        self.assertEqual(gcb_all_share_index, 3.504)


if __name__ == '__main__':
    unittest.main()