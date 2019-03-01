"""  Write a python program to access environment variables.  """

import os
# environ is representing string environment
print(os.environ)
# pathname of home directory
print(os.environ['HOME'])
print(os.environ['PATH'])
print(os.environ['LANG'])
print(os.environ['USER'])
