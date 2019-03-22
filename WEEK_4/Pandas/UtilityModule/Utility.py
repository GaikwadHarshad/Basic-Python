import pandas as pd
import numpy as np


class UtilityClass:
    # create empty series structure
    data = pd.Series()
    data2 = pd.Series()

    def series_data(self, n):
        # iterate over loop
        for x in range(n):
            # getting element from user
            element = int(input("Enter element:"))
            # add element into data Series
            self.data.at[x] = element
        return self.data

    def series_data2(self, n):
        # iterate over loop
        for x in range(n):
            # getting element from user
            element = int(input("Enter element:"))
            # add element into data Series
            self.data2.at[x] = element
        return self.data2

    @staticmethod
    def series_addition(data1, data2):
        dt = data1 + data2
        return dt

    @staticmethod
    def series_subtract(data1, data2):
        return data1 - data2

    @staticmethod
    def series_multiplication(data1, date2):
        return data1 * date2

    @staticmethod
    def series_division(data1, data2):
        return data1 / data2

    @staticmethod
    def get_power():
        data = np.arange(7)
        print(data)
        return np.power(data, 3)
