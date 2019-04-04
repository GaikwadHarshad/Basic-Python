""" Write a Python program to print a dictionary in table format. """

from myprograms.Utility import UtilityDS


class Table:
    # create dictionary of 5 elements
    d = {1: ["Harsh", 22, "Maharastra"],
         2: ["Vikas", 23, "Bihar"],
         3: ["Ishvar", 22, "Gujarat"],
         4: ["Suraj", 23, "Karnatak"],
         5: ["Akash", 22, "Goa"]}

    # function to perform dictionary in format in table
    def table_format(self):
        try:
            print("{:<8} | {:<15} | {:<10} | {:15}".format('POS', 'NAME', 'AGE', 'ADDRESS'))
            print("---------------------------------------------------")
            # function call to print dictionary into table format
            UtilityDS.dict_to_table(self.d)
        except Exception as e:
            print(e)


# instance creation
Table_object = Table()
Table_object.table_format()
