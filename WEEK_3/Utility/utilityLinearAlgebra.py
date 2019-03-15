
# ----------------------------------Linear Algebra----------------------------------------------


class LinearAlgebra:

    def __init__(self):
        self.result = []

    # function for add matrices
    def add_matrices(self, matrix_1, matrix_2):
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in range(len(matrix_1)):
            for col in range(len(matrix_1[0])):
                # add two matrices in resultant matrix
                self.result[row][col] = matrix_1[row][col] + matrix_2[row][col]
        return self.result

    # function for getting scalar matrix
    @staticmethod
    def scalar_matrix(matrix_1, num):
        for row in range(len(matrix_1)):
            for col in range(len(matrix_1[0])):
                # getting scalar matrix by multiplying with number
                matrix_1[row][col] = matrix_1[row][col] * num
        return matrix_1




