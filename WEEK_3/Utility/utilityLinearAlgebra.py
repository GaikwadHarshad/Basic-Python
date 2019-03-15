
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

# multiplication of matrices
    def multiply_matrix(self, matrix_1, matrix_2):
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in range(len(matrix_1)):
            for col in range(len(matrix_1[0])):
                # add two matrices in resultant matrix
                self.result[row][col] = matrix_1[row][col] * matrix_2[row][col]
        return self.result

 # transpose of matrix
    def transpose_matrix(self, matrix_1):
        self.result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for row in range(len(matrix_1)):
            for col in range(len(matrix_1[0])):
                self.result[col][row] = matrix_1[row][col]
        return self.result

    @staticmethod
    def get_matrix_minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    @staticmethod
    def get_matrix_determinant(m):
        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinants = (m[0][0] * (m[1][1] * m[2][2] - m[2][1] * m[1][2])
                        - m[1][0] * (m[0][1] * m[2][2] - m[2][1] * m[0][2])
                        + m[2][0] * (m[0][1] * m[1][2] - m[1][1] * m[0][2]))
        return determinants

    def get_inverse_matrix(self, m):
        determinant = self.get_matrix_determinant(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of co_factors
        co_factors = []
        for r in range(len(m)):
            co_factor_row = []
            for c in range(len(m)):
                minor = self.get_matrix_minor(m, r, c)
                co_factor_row.append(((-1) ** (r + c)) * self.get_matrix_determinant(minor))
            co_factors.append(co_factor_row)
        co_factors = self.transpose_matrix(co_factors)
        for r in range(len(co_factors)):
            for c in range(len(co_factors)):
                co_factors[r][c] = co_factors[r][c] / determinant
        return co_factors

# ---------------------------------------------------------------------------------------------

