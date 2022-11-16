import unittest

from day3 import Day3

day3 = Day3()


class TestDay3(unittest.TestCase):

    def test_basic(self):
        output_string = ['0', '8']
        self.assertTrue(day3.crack_pincode("0") == output_string)

    def test_multi_digit_code(self):
        output_string = ['004', '007', '008', '084', '087', '088', '804', '807', '808', '884', '887', '888']
        self.assertTrue(day3.crack_pincode("007") == output_string)

