import unittest
from coin import Coin

class CoinTests(unittest.TestCase):
    """test the Coin class"""
    def setUp(self):
        self.coin = Coin(1, "Bitcoin", "BTC", 160572147215, 9037.88)

    def test_get_price(self):
        """test that the get_price method returns the correct price"""
        self.assertEqual(self.coin.get_price(), 9037.88)

    def test_all_data(self):
        """test that the all_data method returns all the correct data"""
        self.assertEqual(self.coin.get_all_data(), [1, "Bitcoin", "BTC", 160572147215, 9037.88])