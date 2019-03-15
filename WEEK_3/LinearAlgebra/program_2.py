""" .Write a program to perform scalar multiplication of matrix and a number
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
    Y = 9	      """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra


# inheriting base class Matrix
class ScalarMatrix:

    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    Y = 9

    # create object of utility LinearAlgebra
    def __init__(self):
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def scalar_multiplication(self):
        try:
            # Display Matrix 1
            print("Matrix X : ""\n")
            # iterate over matrix X
            for value in range(len(self.X)):
                print(self.X[value])
            print("-------------------")
            print("Number is : 9")
            print("-------------------")
            # getting scalar multiplication of a matrix
            scalar = self.util.scalar_matrix(self.X, self.Y)
            print("Scalar Matrix Multiplication X :""\n")
            # iterate over addition matrix
            for value in range(len(scalar)):
                print(scalar[value])
        except Exception as e:
            print(e)


# instantiation
ScalarMatrix_object = ScalarMatrix()
ScalarMatrix_object.scalar_multiplication()
