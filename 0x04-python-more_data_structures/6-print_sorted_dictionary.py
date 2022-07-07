#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = list(a_dictionary.keys())
    for k in sorted(ord_list):
        print(f"{k}: {a_dictionary.get(k)}")
