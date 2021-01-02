from random import randint


class Matrix:
    def __init__(self, strings, columns, ):
        self.strings = strings
        self.columns = columns

    def matrix_count_elements(self):
        size = self.strings * self.columns
        return size

    def matrix_creation(self):
        matrix = [[randint(0, 100) for x in range(self.columns)] for i in range(self.strings)]
        return matrix


matrix1 = Matrix(6, 5)
matrix2 = Matrix(7, 6)
print(matrix1.matrix_creation())
print(matrix2.matrix_creation())

