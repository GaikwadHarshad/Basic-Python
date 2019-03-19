""" Write a program to find inverse matrix of matrix X in problem 1 """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra
from myprograms.WEEK_3.LinearAlgebra.BaseMatrix import Matrix


# inherit Matrix base class to InverseMatrix child class
class InverseMatrix(Matrix):

    # constructor for passing child class object to parent class and create object of utilityLinearAlgebra
    def __init__(self):
        super(InverseMatrix, self).__init__()
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def inverse_matrix(self):
        try:
            print("Original Matrix : ")
            for v in range(len(self.x)):
                print(self.x[v])

            # getting inverse of matrix
            c = self.util.get_inverse_matrix(self.x)
            print("Inverse of matrix : ")
            for value in range(len(c)):
                print(c[value])
        except Exception as e:
            print(e)


# instantiation
InverseMatrix_object = InverseMatrix()
InverseMatrix_object.inverse_matrix()
