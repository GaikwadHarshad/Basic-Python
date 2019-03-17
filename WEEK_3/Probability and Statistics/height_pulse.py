""" The table below shows the height, x, in inches and the pulse rate, y, per minute,
    for 9 people. Write a program to find the correlation coefficient and interpret your result.
    x ⇒ 68 72 65 70 62 75 78 64 68
    y ⇒ 90 85 88 100 105 98 70 65 72 """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class HeightPulseRate(ProbabilityStatistics):
    def __init__(self):
        super(HeightPulseRate, self).__init__()
        # height in inches
        self.X = [68, 72, 65, 70, 62, 75, 78, 64, 68]
        # pulse rate per minute
        self.Y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
        # # of cases
        self.N = 9

    # function to calculate coefficient of correlation
    def get_correlation_coefficient(self):
        print("Height in inches X      : ", self.X)
        print("Pulse rate per minute Y : ", self.Y)
        # getting mean value of x
        print("-------------------------------------------------------------")
        x_mean = ProbabilityStatistics.get_mean(self, self.X, self.N)
        print("Mean value of X : ", x_mean)
        # get values X minus mean of X
        print("-------------------------------------------------------------")
        x_bar = ProbabilityStatistics.get_x_bar(self, self.X, x_mean)
        print("X-X bar(x) is : ", x_bar)
        # getting mean value of y
        print("-------------------------------------------------------------")
        y_mean = ProbabilityStatistics.get_mean(self, self.Y, self.N)
        print("Mean value of Y : ", y_mean)
        # get values Y minus mean of Y
        print("-------------------------------------------------------------")
        y_bar = ProbabilityStatistics.get_x_bar(self, self.Y, y_mean)
        print("Y-Y bar(y) is : ", y_bar)
        # getting x^x values
        print("-------------------------------------------------------------")
        x_square = ProbabilityStatistics.get_x_y_square(self, x_bar)
        print("Square of x^x : ", x_square)
        # get sum of x^x values
        print("-------------------------------------------------------------")
        sum_of_x = ProbabilityStatistics.get_sum_of_square(self, x_square)
        print("Sum of x square : ", sum_of_x)
        # get y^y values
        print("-------------------------------------------------------------")
        y_square = ProbabilityStatistics.get_x_y_square(self, y_bar)
        print("Square of y^y : ", y_square)
        # get sum of y^y values
        print("-------------------------------------------------------------")
        sum_of_y = ProbabilityStatistics.get_sum_of_square(self, y_square)
        print("Sum of y square : ", sum_of_y)
        # calculating coefficient of correlation
        print("-------------------------------------------------------------")
        coefficient = ProbabilityStatistics.get_coefficient_of_correlation(self, sum_of_x, sum_of_y)
        print("Coefficient of correlation : ", coefficient)


# instantiation
HeightPulseRate_object = HeightPulseRate()
HeightPulseRate_object.get_correlation_coefficient()
