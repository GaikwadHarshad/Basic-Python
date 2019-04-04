""" Write a program to perform multiplication of given matrix and vector
    X = [[ 5, 1 ,3],
        [ 1, 1 ,1],
        [ 1, 2 ,1]],
    Y = [1, 2, 3] """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra


class MultiMatrices:
    # two matrices declare and initialize
    x = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
    y = [[1], [2], [3]]
    multiplication = [0] * len(x)

    # init function to create object of utility LinearAlgebra
    def __init__(self):
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def vector_matrices(self):
        try:
            # Display Matrix 1
            print("Matrix X : ""\n")
            # iterate over matrix 1
            for value in range(len(self.x)):
                print(self.x[value])
            print("-------------------")
            # Display Vector
            print("Vector y : ""\n")
            # iterate over matrix 2
            for value in range(len(self.y)):
                print(self.y[value])
            print("--------------------")
            # getting multiplication of matrix and vector
            self.multiplication = self.util.vector_matrix(self.x, self.y)
            print("Multiplication of Vector and Matrix :""\n")
            # iterate over addition matrix
            for value in range(len(self.multiplication)):
                print(self.multiplication[value])
        except Exception as e:
            print(e)


# instantiation
MultiMatrices_object = MultiMatrices()
MultiMatrices_object.vector_matrices()
