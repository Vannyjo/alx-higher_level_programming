#!/usr/bin/python3
"""
this module contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance or inherited from a_class"""
    return (isinstance(obj, a_class))
