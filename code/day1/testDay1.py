import unittest
import numpy.testing

import day1
import numpy as np

day1 = day1.Day1()


class TestDay1(unittest.TestCase):

    def test_insufficient_number_of_products(self):
        shopping_cart = [10.75, 11.68]
        self.assertFalse(day1.discount(shopping_cart))

    def test_single_product_discount(self):
        shopping_cart = [68.74, 55.99, 17.85]
        output_shopping_cart = np.array([60.13, 48.98, 15.62])
        self.assertTrue((day1.discount(shopping_cart) == output_shopping_cart).all())

    def test_single_product_discount_with_more_than_three_products(self):
        shopping_cart = [68.74, 55.99, 98.09, 17.85]
        output_shopping_cart = [63.64, 51.84, 90.81, 16.53]
        self.assertTrue((day1.discount(shopping_cart) == output_shopping_cart).all())

    def test_multiple_products_discount(self):
        shopping_cart = [5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]
        output_shopping_cart = [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
        self.assertTrue((day1.discount(shopping_cart) == output_shopping_cart).all())
