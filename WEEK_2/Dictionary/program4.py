""" Write a Python program to iterate over dictionaries using for loops. """

from myprograms.Utility.UtilityDS import dictionaries


class Iterate:
    # iterating over dictionaries using for loop
    def iterate_by_loop(self):
        d = dictionaries()
        # loop to iterate over the dictionary
        for iterate in d:
            print(iterate)


# creating instance
iterate_dict = Iterate()
iterate_dict.iterate_by_loop()
