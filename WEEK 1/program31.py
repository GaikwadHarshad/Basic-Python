""" Write a Python program to get system command output.  """

import subprocess
# run the processes and collect output
get_output = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
# display output of command on terminal
print("List command : ", get_output)




