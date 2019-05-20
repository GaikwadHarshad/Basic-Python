"""  Write a Python program to check multiple keys exists in a dictionary. """
# Utility module for getting functions to use
from myprograms.Utility import UtilityDS


class KeyCheck:
    # dictionary initialisation
    d = {'city': 'pune',
         'country': 'india',
         'state': 'maharastra'}

    # function for checking multiple key
    def check_key(self):
        d1 = {'city', 'pune'}
        d2 = {'state', 'city'}
        d3 = {'city', 'country'}
        try:
            # display original dictionary
            print("Dictionary : ", self.d)
            print("1. check keys :", d1, "\n""2: check keys : ", d2, "\n""3: check keys : ", d3)
            # passing keys as dictionaries to function for getting multiple keys existence result
            check = UtilityDS.check_mul_key(self.d, d1, d2, d3)
            print("Multiple Keys exist in dictionary : ", check)
        except Exception as e:
            print(e)


# instance creation
KeyCheck_object = KeyCheck()
KeyCheck_object.check_key()
