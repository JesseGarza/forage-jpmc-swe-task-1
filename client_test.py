import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Get the price from the first quote
    price = quotes[0]['top_ask']['price']

    # Perform your calculations
    calculated_price = price * 0.5  # Example calculation

    expected_price = 60.6  # Example expected value
    delta = 0.01  # Define the maximum difference allowed between the expected and calculated values
    self.assertAlmostEqual(calculated_price, expected_price, delta=delta)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    # Get the bid and ask prices from the first quote
    bid_price = quotes[0]['top_bid']['price']
    ask_price = quotes[0]['top_ask']['price']

    # Add the assertion
    self.assertGreater(bid_price, ask_price)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
