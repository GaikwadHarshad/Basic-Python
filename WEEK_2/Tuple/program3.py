""" Write a Python program to unpack a tuple in several variables """

from myprograms.Utility import UtilityDS


class Unpack:
    # packing tuple
    tuple1 = (5, 10, 15)

    def unpack_tuple(self):
        try:
            print("Packed tuple : ", self.tuple1)
            # unpacking tuple
            unpack = UtilityDS.unpack_tuple(self.tuple1)
            print("Unpacking tuple : ", unpack)
            u1, u2, u3, u4 = self.tuple1
        except Exception:
            print("Should have enough value to unpack ")


# creating instance
Unpack_object = Unpack()
Unpack_object.unpack_tuple()

