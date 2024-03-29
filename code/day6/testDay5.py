import unittest

from day6 import Day6

day6 = Day6()


class TestDay6(unittest.TestCase):

    def test_1(self):
        self.assertTrue(day6.bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]) == (0, 25))

    def test_2(self):
        self.assertTrue(day6.bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]) == (0, 0))

    def test_3(self):
        self.assertTrue(day6.bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) == (21, 13))

    def test_4(self):
        self.assertTrue(day6.bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]) == (8, 35))
