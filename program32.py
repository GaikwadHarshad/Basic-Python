""" Write a Python program to get the effective group id, effective user id, real group id,
    a list of supplemental group ids associated with the current process.
    Note: Availability: Unix. """

import os
# get effective group id
print("Effective group id : ", os.getegid())
# get effective user id
print("Effective user id : ", os.geteuid())
# get real group id
print("Real group id : ", os.getgid())
# get list of groups
print("List of group : ", os.getgroups())

