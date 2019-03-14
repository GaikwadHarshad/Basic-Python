"""  Write a program to get execution time for a Python method. """

# import time module
import time


def python_method(num):
    # get starting time of method
    start = time.time()
    sum1 = 0
    for e_t in range(1, num+1):
        # sum of the numbers
        sum1 = sum1 + e_t
        # get ending time of method
        end = time.time()
    # return sum and total execution time of method
    return sum1, end-start


number = 10
# method calling and display time on console
print("The sum  and of execution time for python method : ", python_method(number))
