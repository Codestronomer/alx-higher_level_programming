#!/usr/bin/python3
# 0-lookup.py
""" File name : 0-lookup.py
    It is not allowed to import any module
"""

def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """
    return dir(obj)
