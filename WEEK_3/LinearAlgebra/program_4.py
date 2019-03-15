""" Write a program to multiply matrices in problem 1 """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra
from myprograms.WEEK_3.LinearAlgebra.program_1 import AddMatrices


# inherit AddMatrices base class to MultiplyMatrices child class
class MultiplyMatrices(AddMatrices):

    # constructor for passing child class object to parent class and create object of utilityLinearAlgebra
    def __init__(self):
        super(MultiplyMatrices, self).__init__()
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def multiply_matrix(self):
        try:
            # getting multiplication of two matrix
            multiply = self.util.multiply_matrix(self.x, self.y)
            print("Multiplication of Matrix X and Matrix Y :""\n")
            # iterate over addition matrix
            for value in range(len(multiply)):
                print(multiply[value])
        except Exception as e:
            print(e)


# instantiation
MultiplyMatrices_object = MultiplyMatrices()
MultiplyMatrices_object.multiply_matrix()
