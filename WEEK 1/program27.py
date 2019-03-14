""" Write a Python program to get the system time. """

import time
# get time as 24 char string format
t = time.asctime(time.localtime(time.time()))
# display system time
print("System time is : ", t)
