""" X is a normally normally distributed variable with mean μ = 30 and standard deviation σ = 4. Write a program to find
    a. P(x < 40)
    b. P(x > 21)
    c. P(30 < x < 35) """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics
from myprograms.Utility.UtilityDS import validate_num


class NormalDistribution(ProbabilityStatistics):
    # __init__() for getting properties from pare nt class
    def __init__(self):
        super(NormalDistribution, self).__init__()
        self.mean = 30
        self.std_deviation = 4

    # function to get probabilities of situations
    def standard_deviation(self):
        print("1. p(x < 40)")
        print("2. p(x > 21)")
        print("3. p(30 < x < 35)")
        print("4. Exit")
        while 1:
            choice = int(input("Enter choice : "))
            valid_choice = validate_num(choice)
            if valid_choice:
                # get probability for p(x < 40)
                if choice == 1:
                    x = 40
                    value_1 = ProbabilityStatistics.get_std_deviation1(self, x, self.mean, self.std_deviation)
                    print("[area to the left of 2.5] : ", value_1)
                # get probability for p(x > 21)
                elif choice == 2:
                    x = 21
                    value_2 = ProbabilityStatistics.get_std_deviation1(self, x, self.mean, self.std_deviation)
                    print("[area to the left of -2.25] : ", value_2)
                # get probability for p(30 < x < 35)
                elif choice == 3:
                    x = 30
                    value_3 = ProbabilityStatistics.get_std_deviation1(self, x, self.mean, self.std_deviation)
                    print("[area to the left of 0] : ", value_3)
                    x1 = 35
                    value_4 = ProbabilityStatistics.get_std_deviation1(self, x1, self.mean, self.std_deviation)
                    print("[area to the left of 1.25] : ", value_4)
                # exiting
                elif choice == 4:
                    exit()
                else:
                    print("Invalid choice")
            else:
                print("Please enter valid choice")


# instantiation
NormalDistribution_object = NormalDistribution()
NormalDistribution_object.standard_deviation()
