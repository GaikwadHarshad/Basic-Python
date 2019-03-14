"""  Write a Python program to convert a list into a nested dictionary of keys """

from myprograms.Utility import UtilityDS


class List2Dict:
    list_name = [1, 2, 3, 4, 5]

    # function to get nested dictionary of keys from list
    def convert(self):
        try:
            print("Original List : ", self.list_name)
            # calling function for convert list to nested dictionary of keys
            convert_list = UtilityDS.list_to_dict(self.list_name)
            print("Nested Dictionary of keys", convert_list)
        except Exception as e:
            print(e)


# instance creation
List2Dict_object = List2Dict()
List2Dict_object.convert()

