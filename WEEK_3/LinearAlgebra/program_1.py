""" . Write a python program to add below matrices
         X = [[12,7,3],
            [4 ,5,6],
            [7 ,8,9]]
        Y = [[5,8,1],
            [6,7,3],
            [4,5,9]]       """

from myprograms.WEEK_3.Utility import utilityLinearAlgebra
from myprograms.WEEK_3.LinearAlgebra.BaseMatrix import Matrix


# inheriting base class Matrix
class AddMatrices(Matrix):
    # passing object of child class to base class and create object of utility LinearAlgebra
    def __init__(self):
        super(AddMatrices, self).__init__()
        self.util = utilityLinearAlgebra.LinearAlgebra()

    def add_matrices(self):
        try:
            # Display Matrix 1
            print("Matrix X : ""\n")
            # iterate over matrix 1
            for value in range(len(self.x)):
                print(self.x[value])
            print("-------------------")
            # Display matrix 2
            print("Matrix Y : ""\n")
            # iterate over matrix 2
            for value in range(len(self.y)):
                print(self.y[value])
            print("--------------------")
            # getting addition of two matrix
            addition = self.util.add_matrices(self.x, self.y)
            print("Addition of Matrix X and Matrix Y :""\n")
            # iterate over addition matrix
            for value in range(len(addition)):
                print(addition[value])
        except Exception as e:
            print(e)


# instantiation of class
AddMatrices_object = AddMatrices()
AddMatrices_object.add_matrices()
