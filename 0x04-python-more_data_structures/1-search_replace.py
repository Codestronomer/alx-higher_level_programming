#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = [replace for v in my_list if v == search else v]
    return n_list
