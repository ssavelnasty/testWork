import unittest

from calculator import yearsAmount

class TestCalculatorFunction(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(yearsAmount(1000, 15, 2000), 7)

    def test_negative(self):
        self.assertNotEqual(yearsAmount(1000, 15, 2000), 6)
        self.assertNotEqual(yearsAmount(1000, 15, 2000), 8)

    def test_sumAmountOnDeposit(self):
        self.assertIsInstance(yearsAmount(1000, 15, 2000), int)

if __name__ == '__main__':
    unittest.main(verbosity=2)