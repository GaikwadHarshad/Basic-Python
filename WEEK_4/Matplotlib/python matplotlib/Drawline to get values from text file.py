from myprograms.Utility.UtilityDS import validate_num
from myprograms.WEEK_4.Matplotlib.Utility.UtilityModule import Utility

import matplotlib.pyplot as plt


# class to perform graphical representation of data using matplotlib
class DrawLineFromTextValue(Utility):
    choice = 0

    def __init__(self):
        super(DrawLineFromTextValue, self).__init__()

    def line_plotting(self):
        print("1.Draw a line using given axis values taken from a text file")
        print("2. Exit")
        print()
        while True:
            try:
                print()
                # accept choice from user
                self.choice = input("Enter choice : ")
                # validate choice number
                valid_choice = validate_num(self.choice)
                if valid_choice:
                    choice = int(self.choice)
                    if choice == 1:
                        # opening file
                        with open("test.txt") as f:
                            # read content from file
                            data = f.read()
                        data = data.split('\n')
                        # get row 0 value to x axis
                        x = [row.split(' ')[0] for row in data]
                        # get row 1 value to y axis
                        y = [row.split(' ')[1] for row in data]
                        # plot data in x y axes
                        plt.plot(x, y)
                        # set label for x axes
                        plt.xlabel('x_axix')
                        # set label for y axes
                        plt.ylabel('y_axix')
                        # title for plotting line
                        plt.title('sample line')
                        # show the figure
                        plt.show()
                    elif choice == 2:
                        exit()
                    else:
                        print("Enter valid choice")
                else:
                    print("Enter only numbers")
            except Exception as e:
                print(e)


# instantiation
DrawLineFromTextValue_object = DrawLineFromTextValue()
DrawLineFromTextValue_object.line_plotting()
