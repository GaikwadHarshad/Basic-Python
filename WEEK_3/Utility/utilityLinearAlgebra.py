
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

# function for multiplication of vector and matrix
    @staticmethod
    def vector_matrix(matrix_1, vector):
        rows = len(matrix_1)
        vector_range = len(vector)
        # create resultant matrix with N rows
        multiplication = [0] * rows
        sum1 = 0
        for r in range(rows):
            # getting each row of matrix
            row = matrix_1[r]
            for value in range(vector_range):
                # multiplying each element of row with each element of vector
                # add get sum of each multiplied element
                sum1 += sum(row[value] * vector[value])
            multiplication[r], sum1 = sum1, 0
        return multiplication



