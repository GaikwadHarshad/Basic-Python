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


