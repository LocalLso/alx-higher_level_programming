#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Python function that prints all
    integers of a list, in reverse order."""

    myl = my_list
    len_myl = len(myl)
    for i in range(1, (len_myl + 1)):
        print("{:d}".format(myl[-i]))
