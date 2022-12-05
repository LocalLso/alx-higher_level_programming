#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Python function that prints all
    integers of a list, in reverse order."""

    if my_list:
        myl = my_list
        myl.reverse()
        len_myl = len(myl)
        for i in range(0, len_myl):
            print("{:d}".format(myl[i]))
