import unittest
from day5 import Day5

day5 = Day5()


class TestDay5(unittest.TestCase):

    def test_basic(self):
        expected_output = [2, 6, 10]
        self.assertTrue(day5.get_items_at([2, 4, 6, 8, 10], "odd") == expected_output)

    def test_first_value_as_odd_counting_from_backwards(self):
        expected_output = ["E", "A", "I"]
        self.assertTrue(day5.get_items_at(["E", "D", "A", "B", "I", "T"], "even") == expected_output)

    def test_special_characters(self):
        expected_output = [")", "*", "^", "$", "@"]
        self.assertTrue(day5.get_items_at([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "even") == expected_output)

    def test_contains_duplicates(self):
        expected_output = ["R", "I", "R", "R", "L"]
        print(day5.get_items_at(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even") )
        self.assertTrue(day5.get_items_at(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even") == expected_output)