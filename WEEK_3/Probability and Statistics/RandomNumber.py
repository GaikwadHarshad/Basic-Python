""" Write a program to find the probability of getting a random number from the interval [2, 7] """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics
from myprograms.Utility.UtilityDS import validate_num


class RandomNumber(ProbabilityStatistics):
    def __init__(self):
        # passing object of child class to parent class constructor
        super(RandomNumber, self).__init__()
        # list of numbers
        self.interval = [2, 3, 4, 5, 6, 7]

    print("---------------------------------------------")
    print("1. Interval of Number : ")
    print("2. Get probability of random number :")
    print("3. Exit")

    # function to get probability of random number
    def get_random_number(self):
        while 1:

            print("----------------------------------------------")
            choice = int(input("Enter your choice : "))
            # validate choice
            valid_choice = validate_num(choice)
            if valid_choice:
                if choice == 1:
                    # display interval from [2, 7]
                    print(self.interval)
                elif choice == 2:
                    # get random number from list of intervals
                    random_number = ProbabilityStatistics.random_number(self, self.interval)
                    print("Random number from Interval : ", random_number)
                    # calculating probability of random number
                    probability = ProbabilityStatistics.random_probability(self, self.interval, random_number)
                    print("Probability of random number is : ", probability)
                elif choice == 3:
                    exit()
                else:
                    print("Invalid choice")
            else:
                print("Enter choice in number")


# instantiation
RandomNumber_object = RandomNumber()
RandomNumber_object.get_random_number()
