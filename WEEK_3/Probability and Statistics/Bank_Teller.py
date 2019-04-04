""" A bank teller serves customers standing in the queue one by one.
    Suppose that the service time XiXi for customer ii has mean EXi=2 (minutes) and Var(Xi)=1.
    We assume that service times for different bank customers are independent.
    Let YY be the total time the bank teller spends serving 50 customers.
    Write a program to find P(90<Y<110) """

from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class BankTeller:
    # mean value
    g_mean = 2
    # standard deviation
    g_standard_deviation = 1 ** 0.5
    # numbers of customer
    g_n = 50

    g_x1 = 90
    g_x2 = 110

    # function for getting probability of of y time
    print(ProbabilityStatistics.probability_customer(g_mean, g_standard_deviation, g_n, g_x1, g_x2))
    z = 0.9207 - 0.793
    print("Probability = ", z)


# instantiation
BankTeller_object = BankTeller()
