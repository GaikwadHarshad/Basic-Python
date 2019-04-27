""" Write a Python program to convert a list to a tuple. """


class ConvertList:
    li = [1, 2, 3, 4, ]

    def convert(self):
        try:
            print("List : ", self.li)
            # list converting to tuple
            t = tuple(self.li)
            print("Tuple : ", t)
        except Exception as e:
            print(e)


ConvertList_obj = ConvertList()
ConvertList_obj.convert()
