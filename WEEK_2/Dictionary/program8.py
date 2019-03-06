""" Write a Python program to create a dictionary from a string.
    Note: Track the count of the letters from the string.
    Sample string : 'w3resource'
    Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} """

from myprograms.Utility import UtilityDS


class Create:
    def dict_create(self):
        try:
            str1 = "independent47"
            print("The String is : ", str1)
            # calling function to convert string into dictionary
            get_value = UtilityDS.create_dict(str1)
            print("converted string into dictionary : ", get_value)
        except Exception as e:
            print(e)


# instance creation
create_object = Create()
create_object.dict_create()
