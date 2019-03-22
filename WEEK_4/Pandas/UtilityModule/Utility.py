import pandas as pd


class UtilityClass:
    # create empty series structure
    data = pd.Series()

    def series_data(self, n):
        # iterate over loop
        for x in range(n):
            # getting element from user
            element = int(input("Enter element:"))
            # add element into data Series
            self.data.at[x] = element
        return self.data
