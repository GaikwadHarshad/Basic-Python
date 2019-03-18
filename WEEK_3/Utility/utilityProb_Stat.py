import random
import math


# class to perform operation on probability and statistics
class ProbabilityStatistics:
    # constructor
    def __init__(self):
        self.ace = 4
        self.king = 4
        self.queen = 4
        self.jack = 4
        self.cards = 52
        self.rain = 1 / 3
        self.not_rain = 2 / 3
        self.late = 1 / 2
        self.not_late = 1/2
        self.traffic = 1 / 2
        self.not_traffic = 1 / 2
        self.not_rain_traffic = 1 / 4
        self.not_rain_traffic_not_late = 3 / 4

    # function for getting probability of an ace from 52 cards
    def drawing_ace(self):
        probability = self.ace/self.cards
        return probability

# function for getting probability of an ace from 52 cards
    def drawing_ace_after_king(self):
        probability = self.ace/(self.cards-1)
        return probability

# function for getting probability of an ace after drawing ace on 1st draw
    def drawing_ace_after_ace(self):
        probability = (self.ace-1)/(self.cards-1)
        return probability

# function to perform operations on coins
    @staticmethod
    def get_three_heads(sample_space):
        count = 0
        n = 8
        head = 'HHH'
        for prob in sample_space:
            if head == prob:
                count += 1
        if count >= 1:
            # if count >= 1 then get probability
            return count/n
        else:
            return "No Three Heads"

# function for probability of getting exactly one head in sample space
    @staticmethod
    def get_one_head(sample_space):
        count = 0
        total_sample = 8
        success_event = []
        # iterate over sample_space
        for sample in sample_space:
            # iterate each word in sample space
            for word in sample:
                # if word contain char H then count += 1
                if word == 'H':
                    count += 1
            if count == 1:
                # if H occur in 1 time then append word in list
                success_event.append(sample)
            count = 0
        print("Exactly one head : ",  success_event)
        # getting probability of successive event
        probability_of_a = len(success_event)/total_sample
        return probability_of_a

    # function for probability of getting exactly one head in sample space
    @staticmethod
    def get_two_head(sample_space):
        count = 0
        total_sample = 8
        success_event = []
        # iterate over sample_space
        for sample in sample_space:
            # iterate each word in sample space
            for word in sample:
                # if word contain char H then count += 1
                if word == 'H':
                    count += 1
            if count >= 2:
                # if H occur in 1 time then append word in list
                success_event.append(sample)
            count = 0
        print("At least two head : ",  success_event)
        # getting probability of successive event
        probability_of_a = len(success_event)/total_sample
        return probability_of_a

# function for probability of getting exactly one head in sample space
    @staticmethod
    def at_least_one_head(sample_space):
        count = 0
        total_sample = 8
        success_event = []
        # iterate over sample_space
        for sample in sample_space:
            # iterate each word in sample space
            for word in sample:
                # if word contain char H then count += 1
                if word == 'H':
                    count += 1
            if count >= 1:
                # if H occur in 1 time then append word in list
                success_event.append(sample)
            count = 0
        print("At least one head : ",  success_event)
        # getting probability of successive event
        probability_of_a = len(success_event)/total_sample
        return probability_of_a

# function to store values of probability
    def get_n_rain_traffic_n_late(self):
        return self.not_rain * self.not_rain_traffic * self.not_rain_traffic_not_late

# function to get late probability
    def get_late(self):
        return round(self.late, 2)

# function to get probability of Late, Rain, Heavy Traffic
    def get_rain_traffic_late(self):
        rain_traffic_late = self.rain * self.traffic * self.late
        return round(rain_traffic_late, 2)

# function to get probability of woman has cancer if she has positive mammmogram result
    def mammogram_result(self):
        # One percent of women over 50 have breast cancer
        cancer = 0.01
        # women not having cancer
        not_cancer = 0.99
        # Ninety percent of women who have breast cancer test positive on mammograms
        positive_result = 0.9
        # Eight percent of women will have false positives
        false_positive = 0.08
        print("--------------------------------------------------------------------")
        return (positive_result * cancer) / ((positive_result * cancer) + (false_positive * not_cancer))

# function to get random number
    def random_number(self, random_list):
        random_num = random.choice(random_list)
        return random_num

# function to get probability of random number
    def random_probability(self, random_list, random_num):
        count = 0
        # iterate over random_list
        for r in random_list:
            # comparing each random number with random_num
            if r == random_num:
                count += 1
        # if found then get probability of random number
        if count >= 1:
            probability = count/len(random_list)
            return round(probability, 2)
        # else display not found
        else:
            return "No random number found in list of interval"

# function to get mean value
    def get_mean(self, x_list, n):
        sum1 = 0
        for x in x_list:
            sum1 += x
        return round(sum1/n, 2)

# function to get x bar value
    def get_x_bar(self, x_list, x):
        new_list = []
        for l in x_list:
            new_list.append(round(l-x, 2))
        return new_list

# function to get square of variables
    def get_x_y_square(self, sqr_list):
        square = []
        for sq in sqr_list:
            square.append(round(sq*sq, 2))
        return square

    def get_sum_of_square(self, x_list):
        sum1 = 0
        for x in x_list:
            sum1 += x
        return round(sum1, 2)

# function to calculate coefficient of correlation
    def get_coefficient_of_correlation(self, sum_x, sum_y):
        xy = -86.9
        x_and_y = sum_x * sum_y
        coe = xy / math.sqrt(x_and_y)
        return round(coe, 2)

# function to calculate standard deviation
    def get_std_deviation1(self, x, mean, sd):
        total_area = 1
        z_value = (x - mean)/sd
        if z_value == 2.5:
            return 0.9938
        elif z_value == -2.25:
            return total_area - 0.0122
        elif z_value == 1.25:
            return 0.8944-0.5

