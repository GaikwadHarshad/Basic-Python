""" Write a Python program to reverse a tuple. """

from myprograms.Utility import UtilityDS


class Tuple10:

    tuple1 = (9, 8, 7, 6, 5, 4, 3, 2, 1)

    # perform to get reverse number
    def reverse_tuple(self):
        try:
            # original tuple
            print("Original Tuple : ", self.tuple1)
            # getting reverse tuple
            rev = UtilityDS.rev_tuple(self.tuple1)
            # display reverse tuple
            print("Reverse Tuple : ", rev)
        except Exception as e:
            print(e)


# instantiation
Tuple10_object = Tuple10()
Tuple10_object.reverse_tuple()
