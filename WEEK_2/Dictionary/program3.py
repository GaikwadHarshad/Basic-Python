""" Write a Python script to concatenate following dictionaries to create a new one.
    Sample Dictionary :
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """

from myprograms.Utility.UtilityDS import concatenate_dict


class Concat:
    # function performing dictionary concatenation
    def concatenate(self):
        try:
            d1 = {1: 10, 2: 20}
            print("First dictionary : ", d1)
            d2 = {3: 30, 4: 40}
            print("Second dictionary : ", d2)
            d3 = {5: 50, 6: 60}
            print("Third dictionary : ", d3)
            # function call to concatenate dictionary
            util = concatenate_dict(d1, d2, d3)
            print("Concatenated dictionary : ", util)
        except Exception as e:
            print(e)


# instance creation
concat_d = Concat()
concat_d.concatenate()

