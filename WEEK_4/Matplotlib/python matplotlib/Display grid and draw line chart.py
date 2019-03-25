""" Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc.
between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
Date,Close
03-10-16,772.559998
04-10-16,776.429993
05-10-16,776.469971
06-10-16,776.859985
07-10-16,775.080017 """

import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num


class CustomizeGrid:

    def draw_line(self):
        data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
                (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
                (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
                (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
                (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

        # Convert datetime objects to Matplotlib dates.
        x = [date2num(date) for (date, value) in data]
        y = [value for (date, value) in data]

        # creates object of figure class
        fig = plt.figure()

        graph = fig.add_subplot(1, 1, 1)

        # Plot the data as a red line with round markers
        graph.plot(x, y, 'r-o')

        # Set the xtick locations
        graph.set_xticks(x)

        # Set the xtick labels(date)
        graph.set_xticklabels(
            [date.strftime("%Y-%m-%d") for (date, value) in data]
        )

        # Set the x axis label
        plt.xlabel('Date')

        # Set the y axis label
        plt.ylabel('Closing Value')

        # Sets a title
        plt.title('Closing stock value of Alphabet Inc.')

        # Customize the grid
        plt.grid(linestyle='-', linewidth='0.5', color='blue')

        # shows the plot
        plt.show()

CustomizeGrid_obj = CustomizeGrid()
CustomizeGrid_obj.draw_line()
