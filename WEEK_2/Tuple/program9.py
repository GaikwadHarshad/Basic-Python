""" Write a Python program to slice a tuple. """

from myprograms.Utility import UtilityDS


class Tuple9:
    tuple1 = (8, 1, 4, 9, 4, 5, 3, 2, 2, 0)

    def slicing(self):
        try:
            print("Tuple : ", self.tuple1)
            # get slicing tuple
            sl = UtilityDS.slice_tuple(self.tuple1)
            print("Slicing tuple :", sl)
        except Exception as e:
            print(e)


# instance creation
Tuple9_obj = Tuple9()
Tuple9_obj.slicing()
