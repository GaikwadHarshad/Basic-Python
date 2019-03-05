""" Write a Python program to get the name of the host on which the routine is running. """

import socket

# get hostname where routine is running
host_name = socket.gethostname()

# display host name
print("host name where your routine is running : ", host_name)
