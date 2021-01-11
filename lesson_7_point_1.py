class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):

        for row in self.matrix_list:

            for n in row:

                print ( f"{n:4}", end=" ")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            
            for i_2 in range(len(other.matrix_list[i])):

                self.matrix_list[i][i_2] = self.matrix_list[i][i_2] + other.matrix_list[i][i_2]

        return Matrix.__str__(self)


matr = Matrix([[4, 2, 5], [-1, 3, 0], [-4, 2, -4], [5, 2, 4]])


printed_matrix = Matrix([[6, -8, 1], [5, 4, 2], [4, 5, 8], [3, 5, 6]])

print(matr)
print(matr.__add__(printed_matrix))

