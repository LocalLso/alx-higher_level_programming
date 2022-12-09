#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ Python script to print matrix. """
    m = matrix
    n = len(m)
    for i in range(0, n):
        m[i]
        for j in m[i]:
            print("{:d}".format(j), end="" if j != m[i][-1] else "")
        print()
