""" Write a Python program to find the available built-in modules. """

# import module sys, textwrap
import sys
import textwrap

# sort system module name
s = sorted(sys.builtin_module_names)

# join modules by string separator
module = ','.join(s)

# wraps text with width 80
print(textwrap.fill(module, width=80))
