#!/usr/bin/python3
# prints all integers of a list, in reverse order
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        i = len(my_list) - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
