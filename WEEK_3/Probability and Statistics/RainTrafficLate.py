"""  In my town, it's rainy one third of the days. Given that it is rainy,
 there will be heavy traffic with probability 12, and given that it is not rainy,
 there will be heavy traffic with probability 14. If it's rainy and there is heavy traffic,
 I arrive late for work with probability 12. On the other hand, the probability of being late
 is reduced to 18 if it is not rainy and there is no heavy traffic.
 In other situations (rainy and no traffic, not rainy and traffic)
 the probability of being late is 0.25. You pick a random day.

    Write a program to find following
        a. What is the probability that it's not raining and there is heavy traffic and I am not late?
        b. What is the probability that I am late?
        c. Given that I arrived late at work, what is the probability that it rained that day? """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics
from myprograms.Utility.UtilityDS import validate_num


class ChainRule(ProbabilityStatistics):
    # __init__() for getting properties from pare nt class
    def __init__(self):
        super(ChainRule, self).__init__()

    # function to get probabilities of situations
    def find_probability(self):
        print("1. What is the probability that it's not raining and there is heavy traffic and I am not late?")
        print(" 2. What is the probability that I am late?")
        print("3. Given that I arrived late at work, what is the probability that it rained that day? ")
        print("4. Exit")
        while 1:
            choice = int(input("Enter choice for getting probability : "))
            valid_choice = validate_num(choice)
            if valid_choice:
                if choice == 1:
                    # getting probability that its not rain,heavy traffic,not late
                    probability1 = ProbabilityStatistics.get_n_rain_traffic_n_late(self)
                    print("Probability for not rain and heavy traffic and not late : ", probability1)
                elif choice == 2:
                    # getting probability that i am late
                    probability2 = ProbabilityStatistics.get_late(self)
                    print("Probability that I am late : ", probability2)
                elif choice == 3:
                    # getting probability that late, rain and heavy traffic
                    probability3 = ProbabilityStatistics.get_rain_traffic_late(self)
                    print("Probability that it rained that day : ", probability3)
                elif choice == 4:
                    exit()
                else:
                    print("Invalid choice")
            else:
                print("Please enter valid choice")


# instantiation
ChainRule_object = ChainRule()
ChainRule_object.find_probability()
