#!/usr/bin/python3
"""This defines a function to check class."""


def is_same_class(obj, a_class):
    """Returns True or False, depending if obj is of type class."""

    if type(obj) == a_class:
        return True
    else:
        return False
