#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Python function that prints all
    integers of a list, in reverse order."""

    if my_list:
        myl = my_list
        #we could use the reverse() method also
        #myl.reverse()
        len_myl = len(myl)
        for i in range(0, len_myl):
            #replace -(i + 1) with myl[i]
            print("{:d}".format(myl[-(i + 1)]))
