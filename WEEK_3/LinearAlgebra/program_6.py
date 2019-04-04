""" Write a program to find transpose matrix of matrix Y in problem 1      """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra
from myprograms.WEEK_3.LinearAlgebra.BaseMatrix import Matrix


# inheriting base class Matrix
class TransposeMatrix(Matrix):

    # create object of utility LinearAlgebra
    def __init__(self):
        super(TransposeMatrix, self).__init__()
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def transpose(self):
        try:
            # Display Matrix 1
            print("Matrix X : ""\n")
            # iterate over matrix X
            for value in range(len(self.x)):
                print(self.x[value])
            print("-------------------")
            # getting transpose of a matrix
            transpose_mat = self.util.transpose_matrix(self.x)
            print("Transpose of Matrix X :""\n")
            # iterate over addition matrix
            for value in range(len(transpose_mat)):
                print(transpose_mat[value])
        except Exception as e:
            print(e)


# instantiation
TransposeMatrix_object = TransposeMatrix()
TransposeMatrix_object.transpose()
