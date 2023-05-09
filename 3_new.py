def calculate_discounted_price(price, discount_rate):
    """
    This function takes in a 'price' and a 'discount_rate' as arguments and returns the discounted price.

    The calculation of the discounted price is done by multiplying the original price with the complement of the discount rate (1 - discount rate).
    """
    discounted_price = price * (1 - discount_rate)
    return discounted_price


import unittest


class TestCalculateDiscountedPrice(unittest.TestCase):
    """
    This class defines a unit test for the 'calculate_discounted_price' function.
    """
    def test_discounted_price(self):
        """
        This method tests if the 'calculate_discounted_price' function returns the expected discounted price for a given input price and discount rate.
        """
        price = 100
        discount_rate = 0.1
        expected_discounted_price = 90
        calculated_discounted_price = calculate_discounted_price(price, discount_rate)
        self.assertEqual(calculated_discounted_price, expected_discounted_price)


if __name__ == '__main__':
    unittest.main()