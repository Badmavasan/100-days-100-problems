import unittest
import numpy as np
from day4 import Day4


class TestDay4(unittest.TestCase):

    def test_minesweeper_ordinary(self):
        mines_matrix = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 0]
        ]
        day4 = Day4(mines_matrix, mode='mines')

        expected_output = np.array([
            [1, 9, 2, 1],
            [2, 3, 9, 2],
            [3, 9, 4, 9],
            [9, 9, 3, 1]
        ])
        day4_bis = Day4(expected_output, mode='converted')
        day4.conversion_minesweeper()
        self.assertTrue(day4.__eq__(day4_bis))

    def test_different_matrix_size(self):
        mines_matrix = [
            [0, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 0]
        ]
        day4 = Day4(mines_matrix, mode='mines')

        expected_output = np.array([
            [1, 9, 2, 1],
            [2, 3, 9, 2],
            [3, 9, 4, 9],
            [9, 9, 3, 1]
        ])
        day4_bis = Day4(expected_output, mode='converted')
        day4.conversion_minesweeper()
        self.assertFalse(day4.__eq__(day4_bis))

    def test_matrix_full_of_mines(self):
        mines_matrix = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        day4 = Day4(mines_matrix, mode='mines')

        expected_output = np.array([
            [9, 9, 9, 9],
            [9, 9, 9, 9],
            [9, 9, 9, 9],
            [9, 9, 9, 9]
        ])
        day4_bis = Day4(expected_output, mode='converted')
        day4.conversion_minesweeper()
        self.assertTrue(day4.__eq__(day4_bis))

    def test_matrix_no_mines(self):
        mines_matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        day4 = Day4(mines_matrix, mode='mines')

        expected_output = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        day4_bis = Day4(expected_output, mode='converted')
        day4.conversion_minesweeper()
        self.assertTrue(day4.__eq__(day4_bis))
