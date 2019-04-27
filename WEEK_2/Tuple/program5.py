""" Write a Python program to find the repeated items of a tuple. """

from myprograms.Utility import UtilityDS


class Tuple5:
    tuple1 = (3, 5, 6, 5, 4, 3)

    # function performing on tuple to get items repeat or not
    def repeat_items(self):
        try:
            print("Tuple1 : ", self.tuple1)
            # function call  to check whether item repeated or not
            find = UtilityDS.get_repeat_items(self.tuple1)
            if find:
                # if repeat item found
                print("Items is repeated : ", find)
            else:
                print("No items are repeated")
        except Exception as e:
            print(e)


# instance create
Tuple5_object = Tuple5()
Tuple5_object.repeat_items()
