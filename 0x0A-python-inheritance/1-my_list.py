#!/usr/bin/python3
# 1-my_list.py
"""Defines a MyList class inherits from list"""


class MyList(list):
    """Represents a MyList class
    
    Args:
        list: class list
    """

    def print_sorted(self):
        """prints the list, but sorted ascending"""
        print(sorted(list.copy()))
