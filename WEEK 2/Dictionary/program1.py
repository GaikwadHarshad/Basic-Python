"""  Write a Python script to sort (ascending and descending) a dictionary by value. """


class Dictionary:
    def sort_dict(self):
        try:
            # export functions corresponding to intrinsic operators
            import operator
            d = {1: 10, 0: 9, 3: 6, 2: 7, 4: 11}
            print("original dictionary is : ", d)
            # sort dictionary in ascending order
            sort_d = sorted(d.items(), key=operator.itemgetter(0))
            print("sorting in ascending order : ", sort_d)
            # sort dictionary in descending order
            sort_d = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
            print("sorting in reverse order : ", sort_d)
        except Exception as e:
            print(e)


# creating class instance
d_obj = Dictionary()
d_obj.sort_dict()
