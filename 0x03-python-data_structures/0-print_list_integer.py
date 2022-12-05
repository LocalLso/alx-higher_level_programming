#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = my_list
    b = len(a)
    for i in range(0, b):
        print("{:d}".format(a[i]))
