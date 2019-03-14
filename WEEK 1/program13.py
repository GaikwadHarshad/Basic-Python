""" Write a Python program to find out the number of CPUs using."""

from subprocess import call
import multiprocessing
# number of cpu using by process
print("CPU's using:", multiprocessing.cpu_count())
# multiple process statistics
call(["mpstat"])
