import unittest

import day2
import numpy as np

day2 = day2.Day2()


class TestDay2(unittest.TestCase):
    """
    [1,2,3,4,5]
    [1,-,3,4,5] => [1,3,4,5]
    [1,3,4,-] => [1,3,4]
    [1,3,-] => [1,3]
    [-,3] => 3
    """
    def test_k_value_lesser_than_n(self):
        self.assertEqual(day2.survivor(5, 7), 3)

    def test_ordinary(self):
        self.assertEqual(day2.survivor(9, 3), 0)
        self.assertEqual(day2.survivor(9, 2), 2)



