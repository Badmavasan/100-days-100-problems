import numpy as np


class Day4:

    def __init__(self, matrix,mode):
        if mode == 'mines':
            self.mines_matrix = np.array(matrix)
            self.converted_matrix = np.empty(shape=self.mines_matrix.shape,dtype='int')
        elif mode == 'converted':
            self.converted_matrix = matrix

    def conversion_minesweeper(self):
        row,column = self.mines_matrix.shape
        for i in range(0,row):
            for j in range(0,column):
                if self.mines_matrix[i,j] == 1:
                    self.converted_matrix[i,j] = 9
                else:
                    self.converted_matrix[i,j] = 0
                    if i+1 < row:
                        self.converted_matrix[i,j] += self.mines_matrix[i+1,j]
                    if i-1 >= 0:
                        self.converted_matrix[i,j] += self.mines_matrix[i-1,j]
                    if j+1 < column:
                        self.converted_matrix[i,j] += self.mines_matrix[i][j+1]
                    if j-1 >= 0:
                        self.converted_matrix[i,j] += self.mines_matrix[i,j-1]
                    if i+1 < row and j+1<column:
                        self.converted_matrix[i,j] += self.mines_matrix[i+1,j+1]
                    if i+1 < row and j-1>=0:
                        self.converted_matrix[i,j] += self.mines_matrix[i+1,j-1]
                    if i-1 >= 0 and j+1<column:
                        self.converted_matrix[i,j] += self.mines_matrix[i-1,j+1]
                    if i-1 >= 0 and j-1>=0:
                        self.converted_matrix[i,j] += self.mines_matrix[i-1,j-1]

    def __eq__(self, other):
        shape_self = self.converted_matrix.shape
        shape_other = self.converted_matrix.shape
        if shape_self != shape_self:
            return False
        for i in range(shape_self[0]):
            for j in range(shape_self[1]):
                if self.converted_matrix[i,j] != other.converted_matrix[i,j]:
                    return False
        return True
