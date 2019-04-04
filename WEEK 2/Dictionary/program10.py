""" Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'},
                {'id': 2, 'success': False, 'name': 'Rabi'},
                {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True """

# get functions from Utility module
from myprograms.Utility import UtilityDS


class CountValues:
    d = [{'id': 1, 'success': True, 'name': 'Lary'},
         {'id': 2, 'success': False, 'name': 'Rabi'},
         {'id': 3, 'success': True, 'name': 'Alex'}]

    # count values associated with keys
    def count_value(self):
        print("Dictionary : ", self.d)
        try:
            # calling function from Utility module to get no. of value associated with key
            dictionary = UtilityDS.count_key_values(self.d)
            print("Number of dictionary have success True: ", dictionary)
        except Exception as e:
            print(e)


# instance creation
CountValues_object = CountValues()
CountValues_object.count_value()
