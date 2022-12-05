#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ Python lists. """

    if my_list:
        myl = my_list
        len_myl = len(myl)
        if idx < 0:
            return (myl)
        elif idx < 0 and idx >= len_myl:
            return (myl)
        else:
            new_list = []
            for i in range(0, len_myl):
                new_list.insert(i, myl[i])
                if i == idx:
                    new_list[i] = element
            return (new_list)
