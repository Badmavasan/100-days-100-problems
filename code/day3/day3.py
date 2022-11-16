import itertools
import numpy as np


class Day3:

    def __init__(self):
        self.matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [-1, 0, -1]
        ])

    def crack_pincode(self, pincode):
        combinations = []
        for i in pincode:
            surrounding_keys = [i]
            value = int(i)
            x_index, y_index = list(zip(*np.where(self.matrix == value)))[0]
            row, column = self.matrix.shape
            if x_index + 1 < column and self.matrix[x_index + 1, y_index] != -1:
                surrounding_keys.append(str(self.matrix[x_index + 1, y_index]))
            if x_index - 1 > 0 and self.matrix[x_index - 1, y_index] != -1:
                surrounding_keys.append(str(self.matrix[x_index - 1, y_index]))
            if y_index + 1 < row and self.matrix[x_index, y_index + 1] != -1:
                surrounding_keys.append(str(self.matrix[x_index, y_index + 1]))
            if y_index - 1 > 0 and self.matrix[x_index, y_index - 1] != -1:
                surrounding_keys.append(str(self.matrix[x_index, y_index - 1]))
            combinations.append(surrounding_keys)
        output = list(itertools.product(*combinations))
        final = [''.join(list(x)) for x in output]
        return sorted(final)
