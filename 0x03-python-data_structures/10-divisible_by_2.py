#!/usr/bin/python3
# finds all multiples of 2 in list
def divisible_by_2(my_list=[]):
    new_list = [True if i % 2 == 0 else False for i in my_list]
    return new_list
