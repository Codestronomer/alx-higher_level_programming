#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = [replace if v == search else v for v in my_list]
    return n_list
