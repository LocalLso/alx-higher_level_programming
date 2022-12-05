#!/usr/bin/python3
def element_at(my_list, idx):
    myl = my_list
    len_myl = len(myl)
    for i in range(0, len_myl):
        if idx < 0 and idx >= len_myl:
            return
        if i == idx:
            return (myl[i])
