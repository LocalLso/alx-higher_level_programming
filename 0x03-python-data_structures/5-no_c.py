#!/usr/bin/python3
def no_c(my_string):
    """ Python function that removes characters """

    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return (new_string)
