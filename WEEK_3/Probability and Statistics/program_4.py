"""  You toss a fair coin three times write a program to find following:
        a. What is the probability of three heads, HHH?
        b. What is the probability that you observe exactly one heads?
        c. Given that you have observed at least one heads, what is the probability that you observe at least two heads?
"""

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics
from myprograms.Utility.UtilityDS import validate_num


# inheriting class ProbabilityStatistics
class TossCoinThreeTimes(ProbabilityStatistics):

    def __init__(self):
        super(TossCoinThreeTimes, self).__init__()
        self.sample_space = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']

    # function to get probability on sample space on coins
    def probability_on_coin(self):
        print("1.View sample space ""\n""2. probability of three heads, HHH")
        print("3.probability that you observe exactly one heads?")
        print("4.probability that you observe at least two heads""\n""5.Exit")
        while 1:
            try:
                print("---------------------------------------------------------------")
                choice = int(input("Enter choice :"))
                print("---------------------------------------------------------------")
                # validating choice
                valid_choice = validate_num(choice)
                if valid_choice:
                    if choice == 1:
                        # display sample space
                        print("Sample Space is : ", self.sample_space)
                    elif choice == 2:
                        # probability of exact three heads
                        three_head = ProbabilityStatistics.get_three_heads(self.sample_space)
                        print("Probability of three heads, HHH : ", three_head)
                    elif choice == 3:
                        # probability of exact one head
                        one_head = ProbabilityStatistics.get_one_head(self.sample_space)
                        print("Probability that you observe exactly one heads : ", one_head)
                    elif choice == 4:
                        # probability of at least two head
                        two_head = ProbabilityStatistics.get_two_head(self.sample_space)
                        print("Probability that you observe at least two heads : ", two_head)
                    elif choice == 5:
                        exit()
                    else:
                        print("Invalid choice")
            except Exception as e:
                print(e)


# instantiation
TossCoinThreeTimes_object = TossCoinThreeTimes()
# method call
TossCoinThreeTimes_object.probability_on_coin()
