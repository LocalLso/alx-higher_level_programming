#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    myl = my_list
    len_myl = len(myl)
    for i in range(0, len_myl):
        if idx < 0:
            return (myl)
        if idx > len_myl:
            return (myl)
        if i == idx:
            myl[i] = element
            return (myl)
