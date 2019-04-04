""" In a communication system each data packet consists of 1000 bits.
    Due to the noise, each bit may be received in error with probability 0.1.
    It is assumed bit errors occur independently.
    Find the probability that there are more than 120 errors in a certain data packet. """
from myprograms.WEEK_3.Utility.utilityProb_Stat import ProbabilityStatistics


class DataPacket:
    # each bit received error
    g_p = 0.1
    # each packet consist of 1000 bits
    g_n = 1000
    # mean of bits
    g_mean = g_n * g_p
    # standard deviation
    g_standard_deviation = (g_p * (1 - g_p)) ** 0.5
    g_x = 120

    # getting probability of 120 error in a certain data packet
    print(ProbabilityStatistics.probability_data_packet(g_mean, g_standard_deviation, g_n, g_x))
    # z score value
    z = 1 - 0.9821
    print("Probability of 120 errors in a certain data packet = ", z)


# instantiation
DataPacket_object = DataPacket()
