"""  Write a Python program to count number of items in a dictionary value that is a list. """

# Utility module for getting function to use
from myprograms.Utility import UtilityDS


class Items:

    d = {'1': ['Mango', 'Apple', 'Banana'],
         '2': ['Red', 'Pink', 'Blue'],
         '3': ['Lotus', 'Rose', 'WhiteFlower']}

    def count_items(self):
        try:
            print("Items in dictionary :", self.d.values())
            # get number of items in dictionary value that is list
            count = UtilityDS.count_items_dict(self.d)
            print("Number of items in dictionary value is : ", count)
        except Exception as e:
            print(e)


# instance creation
Items_object = Items()
Items_object.count_items()

