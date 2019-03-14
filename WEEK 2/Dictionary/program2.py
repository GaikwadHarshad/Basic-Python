""" Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} """

# import method from Utility
from myprograms.Utility import UtilityDS


# class to perform operation on dictionary
class Dictionary_2:

    def add_key(self):
        try:
            dict = {1: 10, 2: 10}
            print("Original dictionary :", dict)
            # function call for adding key to dictionary
            k = UtilityDS.add_key_dictionary(dict)
            print("After adding key : ", k)
        except Exception as e:
            print(e)


# creating instance
d = Dictionary_2()
d.add_key()
